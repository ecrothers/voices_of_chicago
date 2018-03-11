# Pull the speakers out of the script, and prompt for assignments

import sys
import re

f = open('script.txt','r')
script = f.read()
f.close()

m = re.findall("\[(.*?)\]", script)

chars = set(m)

mapping = ""

# Mappings: F (female), M (male), B (both/unassigned)

for act in chars:
    print (act)
    gender = input("Gender? (F/M/B)")
    mapping += ("{}:{}".format(gender, act) + "\n")

print (mapping)

