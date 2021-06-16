# Data Science Project

Python based tool for automatically building a frequency table based on the Enron corpus.
The frequency table utilizes a n-gram, and retrieves the following information for each n-gram:
1. The number of occurrences.
2. The location of each occurrence.

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
This project relies on the the Natural Language Toolkit (NLTK) to be [installed](https://www.nltk.org/data.html "NLTK installation guide.").

## Usage
Use python3 to run the program, the following three arguments are optional:
1.  -o: The name of the output file, defaults to "frequency_table.pkl"
2.  -i: The location of the input directory. This is the directory from which the program will recursively iterate over each file, defaults to the location of the program.
3.  -n: The n to be used in the n-gram, defaults to 3.

For instance:
```
python3 freqTable.py -o output -i /directory/subdir -n 5
```
Builds a frequency table using a 5-gram of the files in ``/directory/subdir``, and stores the result in ``output.pkl``.

## Data
Attachments and meta-data files are ignored, also a basic filtering is done to eliminate as much noise/headers of the emails as possible.

## Output
The output of the program is a hashmap, which maps a n-gram (key) to a set of filenames (value). Resulting hashmap of type <(String1, String2, ..., StringN),{String}> (<key,value>) is serialized using the Python module [pickle](https://docs.python.org/3/library/pickle.html "Pickle documentation"). The size of the set of filenames would then indicate the frequency of each n-gram.

In order to demonstrate how the .pkl file, as provided by the output of ``freqTable.py``, could be deserialized the script ``deserialize.py`` can be referenced. This script prints the first 10 n-grams of such a .pkl file.

### Usage
Use python3 to run the program, the following argument is required:
1.  -i: The location of the input file. 

For instance:
```
python3 deserialize.py -i output.pkl
```
Will deserialize the file ``output.pkl``, and print the first 10 n-grams.

Note that the pickle module is [insecure](https://docs.python.org/3/library/pickle.html "Pickle documentation"), and only trusted data should be deserialized.
