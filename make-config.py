# -*- coding: utf-8 -*-

import argparse
import configparser
from importlib import import_module
from jinja2 import Environment, FileSystemLoader
import os
import sys

directory = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description="panorama tour configuration")
parser.add_argument("config_module", help="configuration module")
parser.add_argument("-c", "--config",
                    default=os.path.join(directory, "config.ini"),
                    help="configuration file")
args = parser.parse_args()

# import module configuration file
try:
    config_module = import_module(args.config_module)
except:
    sys.stderr.write("problem encountered while processing module %s\n" % args.config_module)
    sys.exit(1)

# read section "saladoplayersettings" in configuration file
config = configparser.ConfigParser()
try:
    config.read(args.config)
    section = config["saladoplayersettings"]
except:
    sys.stderr.write("problem encountered while processing configuration file %s\n" % args.config)
    sys.exit(2)

context = {
    "tour": config_module.tour,
    "saladoplayersettings": {
        "branding": section.getboolean("branding", True),
        "debug": section.getboolean("debug", False),
        "static_image_path": section.get("static_image_path"),
        "goto_hotspot_image": section.get("goto_hotspot_image", "goto.png"),
        "info_hotspot_image": section.get("info_hotspot_image", "info.png"),
        "link_hotspot_image": section.get("link_hotspot_image", "link.png"),
        "see_hotspot_image": section.get("see_hotspot_image", "see.png"),
        "url": section.get("url", "http://www.pano.com"),
    },
}

env = Environment(loader=FileSystemLoader(os.path.join(directory, "templates")))
template = env.get_template("config.xml")
output_from_parsed_template = template.render(context)

# to save the results
for line in output_from_parsed_template.splitlines():
    line = line.rstrip()
    if line:
        line = line + '\n'
        sys.stdout.write(line)
