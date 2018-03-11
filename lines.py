import sys
import re
import csv
from collections import defaultdict
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from util import TwoBarChart

# Open the script and load it
f = open('script.txt','r')
script = f.read()
f.close()

roles = {} 

# Load mapping of male/female characters
with open('genders.txt', 'r') as csvfile:
    genreader = csv.reader(csvfile, delimiter=':')
    for row in genreader:
        roles[row[1]] = row[0]
        
# Split out lines by [Speaker]
rawlines = script.split("\n\n")
lines = defaultdict(list)

for line in rawlines:
    speaker = line.split("\n")[0][1:-1]
    lines[speaker].extend(line.split("\n")[1:])

femalelines = []
malelines = []
unasslines = []

#print(roles)

# Separate based on gender
for speaker in lines:
    if (roles[speaker] == "M"):
        malelines.extend(lines[speaker])
    elif (roles[speaker] == "F"):
        femalelines.extend(lines[speaker])
    else:
        unasslines.extend(lines[speaker])

# Literally count the number of newlines as lines.
# This is actually a pretty bad measure due to the songs lyrics, and many lines being split partway.
# We'll instead use the word count
"""
print("\nAttributed to male characters\n====================")
print(malelines)

print("\nAttributed to female characters\n====================")
print(femalelines)

print("\nAttributed to 'both'\n====================")
print(unasslines)

print("Male characters: {} lines".format(len(malelines)))
print("Female characters: {} lines".format(len(femalelines)))
print("Unassigned: {} lines".format(len(unasslines)))
"""

# Flatten arrays for a crude word count
flatmale = ""
flatfemale = ""
flatunass = ""

for line in malelines:
    flatmale += (line + " ")

for line in femalelines:
    flatfemale += (line + " ")

for line in unasslines:
    flatunass += (line + " ")

mcount = len(flatmale.split())
fcount = len(flatfemale.split())
ucount = len(flatunass.split())

print("\nFinal breakdown:\n====================")
print("Male characters: approximately {} words".format(mcount))
print("Female characters: approximately {} words".format(fcount))
print("Unassigned: approximately {} words\n".format(ucount))

# Visualization (requires libraries), comment out if not desired
TwoBarChart.draw(mcount, fcount)

