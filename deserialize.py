from sys import argv, exit
from getopt import getopt, GetoptError
from os import path
from pickle import load
from itertools import islice

def init():
    inputFile = ""

    try:
        opts, args = getopt(argv[1:],"hi:")
    except GetoptError:
        print ('deserialize.py -i <inputfile>')
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('deserialize.py -i <inputfile>')
            exit()
        elif opt in ("-i"):
            inputFile = arg
            if not path.exists(inputFile):
                print('The input file does not exist.')
                exit()
            if not path.isfile(inputFile):
                print('The input is not a file.')
                exit()
    
    if inputFile == "":
        print('Usage: deserialize.py -i <inputfile>')
        exit()

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
