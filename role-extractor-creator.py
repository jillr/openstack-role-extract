#!/usr/bin/env python

import yaml
import pprint
import os

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

def yaml_dump(filepath, data):
## TODO: better format data output
    """ Dumps YAML to a file """
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

pp = pprint.PrettyPrinter(width=76)


## Write gathered data to new yaml
## TODO: dont hardcode thinsg
overwrite = True
def write_role_data(role_dir, task_name, task_data):
    overwrite = True
    try:
        if os.path.exists(role_dir):
            pass
            #todo: handle whether to write to an existing directory
            #with open('test.yaml', wb) as f:
            #yaml_dump('test.yaml', foo_role_data)
        #elif os.path.exists(foo_dir): # FIXME
        #    print("Did you mean to write here?  Set the overwrite flag")
        else:
# if the dir doesnt exist, make it and write yaml in it 
# TODO: be more graceful about making keystone/tasks a var for reuse
            os.makedirs(role_dir+'/tasks/')
            yaml_dump(role_dir+'/tasks/'+task_name+'.yaml', task_data)
    except os.error as e:
        print("I can't write here")


if __name__ == "__main__":
    filepath = options.filename
    data = yaml_load(filepath)

    outputs_data = data.get("outputs")

    role_data = outputs_data.get("role_data")

    role_values = role_data.get("value")
    upgrade_tasks_data = role_values.get("upgrade_tasks")
#    print(type(upgrade_tasks_data))
#    for i in upgrade_tasks_data:
#        #print(i.items())

    ff_upgrade_tasks_data = role_values.get('fast_forward_upgrade_tasks')
#    print(type(ff_upgrade_tasks_data))
#    for i in ff_upgrade_tasks_data:
#        print(i.items())
    task_name = 'fast_forward_upgrade_tasks'
    role_dir = 'keystone'
    write_role_data(role_dir, task_name, ff_upgrade_tasks_data)

## TODO: add an overwrite flag
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
