# Data Science Project

Python based tool for automatically building a frequency table based on the Enron corpus.
The frequency table utilizes a n-gram, and retrieves the following information for each n-gram:
1. The number of occurences.
2. The location of the occurences.

## Example
If an n-gram of n=3 is used, then the sentence
```
We like to go to the beach.
```
has the following 3-gram
```
We like to, like to go, to go to, go to the, to the beach.
```

## Requirements
Python 3.8+ needs to be installed.
This project relies on the The Natural Language Toolkit (NLTK) to be [installed](https://www.nltk.org/data.html "NLTK installation guide.").

## Usage
Use python3 to run the program, the following three arguments can be optionally supplied:
1.  -o: The name of the output file, defaults to "frequency_table.pkl"
2.  -i: The location of the input directory. This is the directory from which the program will recursively iterate over each file, defaults to the location of the program.
3.  -n: The n to be used in the n-gram, defaults to 3.
For instance:
```
python3 freqTable.py -o output -i /directory/subdir -n 5
```
Builds a frequency table using a 5-gram of the files in ``/directory/subdir``, and store the result in ``output.pkl``.

### Data
Attachments and meta-data files are ignored, also a basic filtering is done to eliminate as much noise/heads of emails as possible.

## Viewing the results
TODO
