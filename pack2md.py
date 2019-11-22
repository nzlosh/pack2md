#!/usr/bin/env python3

# pack2md.py creates pack README.md file from pack metadata.
# Copyright (C) 2019  Carlos <nzlosh@yahoo.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import argparse

import yaml
from jinja2 import Environment, FileSystemLoader


def fetch_template(template="README.jinja", template_dir="."):
    print("Fetching template ...")
    file_loader = FileSystemLoader(template_dir)
    env = Environment(loader=file_loader)
    return env.get_template(template)


def fetch_yaml(dirname, display):
    print("Fetching {} ...".format(display))
    items = {}
    if os.path.exists(dirname):
        for e in os.listdir(dirname):
            if e.endswith(".yaml"):
                with open("{}/{}".format(dirname, e), "r") as f:
                    items[e] = yaml.load(f, Loader=yaml.FullLoader)
    return items


def render_document(template, data, filename):
    if not os.path.exists(f"{filename}.bak") and os.path.exists(f"{filename}"):
            os.replace(f"{filename}", f"{filename}.bak")
    with open(filename, "w") as f:
        f.write(template.render(data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create README markdown from pack metadata.")
    parser.add_argument("pack_path", type=str, help="Path to StackStorm pack.")
    args = parser.parse_args()

    if os.path.exists(args.pack_path):
        render_document(
            fetch_template(template_dir=args.pack_path),
            {
                "pack": fetch_yaml(args.pack_path, "pack meta"),
                "actions": fetch_yaml(f"{args.pack_path}/actions", "action meta"),
                "sensors": fetch_yaml(f"{args.pack_path}/sensors", "sensor meta")
            },
            f"{args.pack_path}/README.md"
        )
    else:
        print("'{}' doesn't exist.".format(args.pack_path))
