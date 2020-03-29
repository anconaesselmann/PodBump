#!/usr/bin/env python3

import os
import re
import sys

from enum import Enum
class Component(Enum):
    PATCH = 2
    MINOR = 1
    MAJOR = 0

type = Component.PATCH

if len(sys.argv) > 1:
	string = sys.argv[1]
	if string == "patch" or string == "p":
		type = Component.PATCH
	elif string == "minor" or string == "min":
		type = Component.MINOR
	elif string == "major"  or string == "maj":
		type = Component.MAJOR

podspec_path = os.path.basename(os.path.normpath(os.getcwd())) + ".podspec"

def bump_version(match):
    version = [
    	int(match.group(2)),
    	int(match.group(3)),
    	int(match.group(4))
    ]

    version[type.value] = version[type.value] + 1

    new_version = str(version[0]) + "." + str(version[1]) + "." + str(version[2])
    print(new_version)
    return match.group(1) + new_version
 
f = open(podspec_path, 'r') 
fileinput = f.readlines()
f.close()

modified = ""

for line in fileinput:
    line_modified = result = re.sub(r'(\.version\s+=\s+\')([0-9]+)\.([0-9]+)\.([0-9]+)', bump_version, line)    
    modified += line_modified

f = open(podspec_path, 'w')
f.write(modified)
f.close()
