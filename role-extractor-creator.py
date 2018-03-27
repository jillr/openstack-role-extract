#!/usr/bin/env python

import yaml
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

if __name__ == "__main__":
    filepath = options.filename
    data = yaml_load(filepath)
    # print(data)

    outputs_data = data.get("outputs")
    # for k, v in outputs_data.items():
        # print("{} = {}".format(k, v))

    role_data = outputs_data.get("role_data")
    # for k, v in role_data.items():
        # print("{} = {}".format(k, v))

    upgrade_tasks_data = role_data.get("upgrade_tasks")
    for k, v in upgrade_tasks_data.items():
        print("{} = {}".format(k, v))



"""
Example format of yaml to be extracted as follows

outputs:
    role_data:
        upgrade_tasks:
        .
        .
        .
        fast_forward_upgrade_tasks:
"""
