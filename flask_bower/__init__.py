# -*- coding: utf-8 -*-
from flask.ext.assets import Bundle
import os

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
    return os.path.join(static_files_folder, component_file_name)


def get_assets_files():
    return [get_component_file_path()]


from asset_helper import create_asset
from bower import get_libraries, get_appication, get_files


def get_assets_by_type(asset_type):
    vendor_assets = get_libraries()
    application_assets = get_appication()
    return Bundle(Bundle(*(vendor_assets[asset_type] if asset_type in vendor_assets else [])),
                  Bundle(*[
                      create_asset(asset)
                      for asset in application_assets[asset_type]
                  ], output='gen/full.'+asset_type) if asset_type in application_assets else Bundle())


def get_assets_by_category_and_type(category, asset_type):
    assets = get_files(category)
    return Bundle(*[
        create_asset(asset)
        for asset in assets[asset_type]
    ], output='gen/full.'+asset_type) if asset_type in assets else Bundle()


def get_css_assets():
    return get_assets_by_type("css")


def get_js_assets():
    return get_assets_by_type("js")
