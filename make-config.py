# -*- coding: utf-8 -*-

import argparse
from importlib import import_module
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(description="panorama tour configuration")
parser.add_argument("config_module", help="configuration module")
args = parser.parse_args()

config_module = import_module(args.config_module)

context = {
    "tour": config_module.tour,
    "saladoplayersettings": {
        "branding": True,
        "debug": False,
        "static_image_path": "/static/images/hotspots",
        "goto_hotspot_image": "pas_orange_blanc_carre.png",
        "info_hotspot_image": "info_bleu_blanc_triangle.png",
        "link_hotspot_image": "oeil_jaune_noir_rond.png",
        "see_hotspot_image": "oeil_jaune_noir_rond.png",
        "url": "http://panoramas.franck-barbenoire.fr",
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
