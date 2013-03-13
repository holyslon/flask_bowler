# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask.ext.assets import Bundle
from flask_bower import filter_by_extension, assets_conversion_map
from os import path


def generate_asset_name(asset_name, asset_ext):
    return asset_name + "." + assets_conversion_map[asset_ext]


def create_asset(path_to_asset):
    asset_name, asset_ext = path.splitext(path_to_asset)
    asset_ext = asset_ext[1:]
    generated_asset_name = generate_asset_name(asset_name, asset_ext)
    return Bundle(path_to_asset,
                  filters=filter_by_extension[asset_ext],
                  output=path.join("gen", generated_asset_name))
