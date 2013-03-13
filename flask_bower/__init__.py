# -*- coding: utf-8 -*-
from flask.ext.assets import Bundle
import sys

__all__ = ['get_css_assets',
           'get_js_assets',
           'get_assets_by_category_and_type',
           'filter_by_extension',
           'assets_conversion_map',
           'static_files_folder',
           'component_file_name',
           ]

filter_by_extension = {
    "coffee": "coffeescript",
    "sass": "sass"
}

assets_conversion_map = {
    "coffee": "js",
    "sass": "css"
}

static_files_folder = "static"
component_file_name = "component.json"


def get_component_file_path():
    return sys.path.join(static_files_folder, component_file_name)


def get_assets_files():
    return [get_component_file_path()]


from asset_helper import create_asset
from bower import get_libraries, get_appication, get_files


def get_assets_by_type(asset_type):
    vendor_assets = Bundle(*get_libraries()[asset_type])
    application_assets = Bundle(*[
        create_asset(asset)
        for asset in get_appication()[asset_type]
    ], output='gen/full.'+asset_type)
    return Bundle(vendor_assets, application_assets)


def get_assets_by_category_and_type(category, asset_type):
    return Bundle(*[
        create_asset(asset)
        for asset in get_files("category")[asset_type]
    ], output='gen/full.'+asset_type)


def get_css_assets():
    return get_assets_by_type("css")


def get_js_assets():
    return get_assets_by_type("js")
