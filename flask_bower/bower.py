# -*- coding: utf-8 -*-
from subprocess import check_output
from flask_bower import assets_conversion_map, static_files_folder, get_component_file_path
from StringIO import StringIO
from json import load
from os import path
from graph import Node, linerise_graph


def read_bower_map():
    bower_map = check_output([
        "bower",
        "list",
        "--map"
    ], cwd=static_files_folder)
    return load(StringIO(bower_map))


def make_list_of_sources(raw_sources):
    sources = list()
    if isinstance(raw_sources, str):
        sources.append(raw_sources)
    else:
        sources.extend(raw_sources)
    return sources


def get_components(map_in_dict):
    for key, value in map_in_dict.iteritems():
        sources = make_list_of_sources(value['source']['main'])
        if 'dependencies' in value:
            yield key, sources, [dep for dep in value['dependencies']]
        else:
            yield key, sources, []


class Component:

    def __init__(self, name, sources, dependencies):
        self.name = name
        self.sources = sources
        self.dependencies = dependencies

    def __lt__(self, other):
        return self.name in other.dependencies

    def __repr__(self):
        return self.name

    def getCssAssetss(self):
        return [asset for asset in self.sources if asset.endswith(".css")]

    def getJsAssetss(self):
        return [asset for asset in self.sources if asset.endswith(".js")]


def group_assets_by_extencion(assets):
    groups = {}
    for asset in assets:
        key = path.splitext(asset)[1][1:]
        if key not in groups:
            groups[key] = []
        groups[key].append(asset)
    return groups


def group_assets_by_conversion_target(assets):
    assets_grouped_by_extension = group_assets_by_extencion(assets)
    groups = {}
    for key, value in assets_grouped_by_extension.iteritems():
        after_convertion_key = assets_conversion_map[key]
        if after_convertion_key not in groups:
            groups[after_convertion_key] = []
        groups[after_convertion_key].extend(value)
    return groups


def get_files(tag):
    app_in_dictionary = {}
    with open(get_component_file_path()) as component_file:
        app_in_dictionary = load(component_file)
    sources = make_list_of_sources(app_in_dictionary[tag])
    return group_assets_by_conversion_target(sources)


def get_appication():
    return get_files('main')


def get_libraries():
    c = list(get_components(read_bower_map()))
    nodes = [(Node((name, files)), dep) for name, files, dep in c]

    def get_node(nodes, node_name):
        for n, _ in nodes:
            if n.data[0] == node_name:
                return n

    for node, deps in nodes:
        for dep in deps:
            parent = get_node(nodes, dep)
            parent.add(node)

    res = list(linerise_graph([n for n, d in nodes if len(d) == 0]))

    return {
        "css": [
            item
            for comp in res
            for item in comp.data[1] if item.endswith(".css")
        ],
        "js": [
            item
            for comp in res
            for item in comp.data[1] if item.endswith(".js")
        ]
    }
