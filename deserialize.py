from sys import argv, exit
from getopt import getopt, GetoptError
from os import path
from pickle import load
from itertools import islice

def init():
    inputFile = ""

    # Get the input arguments.
    try:
        opts, args = getopt(argv[1:],"hi:")
    # Unexpected arguments are provided.
    except GetoptError:
        print ('deserialize.py -i <inputfile>')
        exit(2)
    # For each provided argument:
    for opt, arg in opts:
        # Help argument.
        if opt == '-h':
            print ('deserialize.py -i <inputfile>')
            exit(2)
        # Input file argument.
        elif opt in ("-i"):
            inputFile = arg
            # Input file must exist.
            if not path.exists(inputFile):
                print('The input file does not exist.')
                exit(2)
            # Input file must also be a file.
            if not path.isfile(inputFile):
                print('The input is not a file.')
                exit(2)
    
    # Ensure that input file is not empty.
    if inputFile == "":
        print('Usage: deserialize.py -i <inputfile>')
        exit(2)

    return inputFile
 
def deserialize(inputFile):
    with open(inputFile, 'rb') as file:
        return load(file)

if __name__ == '__main__':
    # Get the input filename.
    inputFile = init()
    # Get the dict.
    deserializedDict = deserialize(inputFile)

    # Use the data, for instance print the first 10 n-grams:
    for key in islice(deserializedDict, 0, 10):
        print(key, "has", len(deserializedDict[key]), "occurrences.")
