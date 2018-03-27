#!/usr/bin/env python

import yaml
import pprint

from optparse import OptionParser

parser = OptionParser("usage: %prog -f --file filename")
parser.add_option("-f", "--file", dest="filename")

(options, args) = parser.parse_args()
if options.filename is None:
    parser.error("please supply yaml filename")

def yaml_load(filepath):
    """ Loads YAML from a file """
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath):
    """ Dumps YAML to a file """
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

pp = pprint.PrettyPrinter(width=76)

if __name__ == "__main__":
    filepath = options.filename
    data = yaml_load(filepath)

    outputs_data = data.get("outputs")

    role_data = outputs_data.get("role_data")

    role_values = role_data.get("value")
    upgrade_tasks_data = role_values.get("upgrade_tasks")
    print(type(upgrade_tasks_data))
    for i in upgrade_tasks_data:
        print(i.items())


"""
Example format of yaml to be extracted as follows

outputs:
    role_data:
        value:
            upgrade_tasks:
            .
            .
            .
            fast_forward_upgrade_tasks:
"""
