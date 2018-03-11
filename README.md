# Voices of "Chicago"

Breakdown of lines by gender within the 2002 movie "Chicago".  Inspired by the [Polygraph project on Dialogue and Film](http://polygraph.cool/films/embed.html).  From the results, it appears to be the only movie to win "Best Picture" in over 25 years with more words spoken by female characters than male characters.

## Requirements

[Python3](https://www.python.org/downloads/)

For visualization, install numpy, matplotlib, python3-tk.

On Debian Linux:

```
sudo apt-get install python3 python3-tk
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
sudo pip3 install numpy
sudo pip3 install matplotlib

```

## Methodology

Data sourced from [the film script available here](http://www.cswap.com/2002/Chicago/song/Full_Script).

The data was sanitized and formatted into the format present in script.txt.  To my knowledge, the script is largely accurate, though minor inaccuracies in wording are likely.

Attributing some lines to characters was somewhat challenging, given the musical nature of the movie and the formatting of the source data.  Some minor lines remain unassigned as the gender of the speaker was not easily obtainable from IMDB, or the line was spoken by a crowd in unison.  Please open an issue if you know the specified gender attributed to an unassigned line.

In the musical number "All I Care About Is Love", lines attributed to "Billy Flynn, girls" have been counted under "Billy Flynn" (other characters are performing backup vocals).

A more rigorous transcription of the script and association of each line would yield more exact results, but the provided data is sufficient to identify the overall division of lines.

## Results

### Final breakdown 

Male characters: approximately 4791 words
Female characters: approximately 6317 words
Unassigned: approximately 79 words
