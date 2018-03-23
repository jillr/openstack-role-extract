#!/usr/bin/env python

import yaml
import pprint
from optparse import OptionParser

parser = OptionParser("usage: %prog -f --file filename")
parser.add_option("-f", "--file", dest="filename")

(options, args) = parser.parse_args()
if options.filename is None:
    parser.error("please supply yaml filename")

pp = pprint.PrettyPrinter(width=76)

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

with open(options.filename, 'r') as stream:
#    print(yaml.dump(yaml.load(stream))) # dumps yaml as-is to stdout
#    pp.pprint(yaml.load(stream)) # Simple dump of the map; not yaml

    dataMap = yaml.load(stream)
    # pp.pprint(dataMap)
    # print(dataMap.get(fast_forward_upgrade_tasks))
