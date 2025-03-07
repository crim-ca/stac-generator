# encoding: utf-8
"""

"""
__author__ = "Richard Smith"
__date__ = "08 Jun 2021"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "richard.d.smith@stfc.ac.uk"

import argparse
import logging

import pkg_resources
import yaml

from stac_generator.core.exceptions import NoPluginsError
from stac_generator.core.generator import BaseGenerator
from stac_generator.core.utils import load_plugins


def command_args():
    """
    Sets the command line arguments and handles their parsing
    :return: command line options
    """
    parser = argparse.ArgumentParser(description="Run the asset scanner as configured")
    parser.add_argument("conf", help="Path to a yaml configuration file")
    args = parser.parse_args()

    return args


def setup_logging(conf):
    config = conf.get("logging", {})
    if not config or (config and not config.get("format")):
        config["format"] = "%(asctime)s %(name)s %(levelname)s %(message)s"

    logging.basicConfig(**config)


def load_config(path):
    with open(path) as reader:
        conf = yaml.safe_load(reader)
    return conf


def load_generator(conf: dict) -> BaseGenerator:
    """
    Load the generator.

    Looks for generator defined in the configuration in preference
    and falls back to the first defined entry point
    at ``stac_generator.generators``

    :param conf: Configuration dict
    :return: Generator
    """

    generator = None

    if conf.get("generator"):
        entry_points = pkg_resources.iter_entry_points(
            "stac_generator.generators", conf.get("generator")
        )

        for entry_point in entry_points:

            generator = entry_point.load()

            # Only load the first one
            break

    if not generator:
        raise NoPluginsError("No extraction plugins have been loaded")

    return generator(conf)


def main():
    args = command_args()

    conf = load_config(args.conf)

    setup_logging(conf)

    generator = load_generator(conf)

    input_plugins = load_plugins(conf, "stac_generator.inputs", "inputs")

    for input_plugin in input_plugins:
        input_plugin.run(generator)


if __name__ == "__main__":
    main()
