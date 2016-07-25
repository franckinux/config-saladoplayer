# -*- coding: utf-8 -*-

import argparse
import configparser
from importlib import import_module
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(description="panorama tour configuration")
parser.add_argument("config_module", help="configuration module")
args = parser.parse_args()

# import module configuration file
config_module = import_module(args.config_module)

# read section "saladoplayersettings" in configuration file
config = configparser.ConfigParser()
config.read("config.ini")
section = config["saladoplayersettings"]

context = {
    "tour": config_module.tour,
    "saladoplayersettings": {
        "branding": section.getboolean("branding"),
        "debug": section.getboolean("debug"),
        "static_image_path": section.get("static_image_path"),
        "goto_hotspot_image": section.get("goto_hotspot_image"),
        "info_hotspot_image": section.get("info_hotspot_image"),
        "link_hotspot_image": section.get("link_hotspot_image"),
        "see_hotspot_image": section.get("see_hotspot_image"),
        "url": section.get("url"),
    },
}

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template("config.xml")
output_from_parsed_template = template.render(context)

# to save the results
with open("config.xml", "wb") as fh:
    for line in output_from_parsed_template.splitlines():
        line = line.rstrip()
        if line:
            line = line + '\n'
            fh.write(line.encode("utf-8"))
