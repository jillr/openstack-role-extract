#!/usr/bin/env python

import yaml
import pprint
import os

from optparse import OptionParser

parser = OptionParser("usage: %prog -f --file filename")
parser.add_option("-f", "--file", dest="filename")
parser.add_option("-r", "--role-name", dest="role_name")
parser.add_option("-o", "--overwrite", dest="overwrite", action='store_true', default=False) 

(options, args) = parser.parse_args()
if options.filename is None:
    parser.error("please supply yaml filename")


def yaml_load(filepath):
    """ Loads YAML from a file """
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath, data):
## TODO: better format data output
    """ Dumps YAML to a file """
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

pp = pprint.PrettyPrinter(width=76)


## Write gathered data to new yaml
def write_role_data(role_dir, task_name, task_data):
    try:
        output_dir = role_dir+'/tasks/'
        if os.path.exists(role_dir) and overwrite:
            print("Override set, writing to existing dir.")
            yaml_dump(output_dir+task_name+'.yaml', task_data)
        elif os.path.exists(role_dir):
            print("{} already exists, skipping. Set the overwrite flag (-o)  
                                    to ignore this error.".format(role_dir))
        else:
        # if the dir doesnt exist, make it and write yaml in it 
            os.makedirs(output_dir)
            yaml_dump(output_dir+task_name+'.yaml', task_data)
    except os.error as e:
        print("I can't write here, because {}".format(e))


if __name__ == "__main__":
    filepath = options.filename
    role_name = options.role_name
    overwrite = options.overwrite
    data = yaml_load(filepath)

    outputs_data = data.get("outputs")

    role_data = outputs_data.get("role_data")

    role_values = role_data.get("value")
    upgrade_tasks_data = role_values.get("upgrade_tasks")

    ff_upgrade_tasks_data = role_values.get('fast_forward_upgrade_tasks')
    task_name = 'fast_forward_upgrade_tasks'
    role_dir = 'keystone'
    write_role_data(role_dir, task_name, ff_upgrade_tasks_data)

## TODO: add the output dir
## TODO: add a flag for what data to extract

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


"""
Example format of role layout on disk

    keystone/
        tasks/
            upgrade_tasks.yaml
            fast_forward_upgrade_tasks.yaml
"""
