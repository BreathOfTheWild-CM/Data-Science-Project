from sys import argv, exit
from getopt import getopt, GetoptError
from os import walk, path
from collections import defaultdict 
from re import sub, search, VERBOSE, DOTALL, MULTILINE
from nltk import sent_tokenize, ngrams, RegexpTokenizer
from pickle import dump

def init():
    # Default output file.
    outputFile = 'frequency_table'
    # Default start directory is the current directory.
    startDir = path.dirname(path.abspath(__file__))
    # Default n for n-gram.
    n = 3

    try:
        opts, args = getopt(argv[1:],"hi:o:n:")
    except GetoptError:
        print ('freqTable.py -i <inputdirectory> -o <outputfile> -n <n>')
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('freqTable.py -i <inputdirectory> -o <outputfile> -n <n>')
            exit()
        elif opt in ("-i"):
            startDir = arg
            if not path.exists(startDir):
                print('The input directory does not exist')
                exit()
            if not path.isdir(startDir):
                print('The input is not a directory.')
                exit()
        elif opt in ("-o"):
            outputFile = arg
        elif opt in ("-n"):
            try :
                n = int(arg)
            except ValueError:
                print("Invalid argument given for n.")
                exit()

    return n, startDir, outputFile
 
def buildFreqTable(n, rootdir):
    # Create the, currently empty dict:
    # Once a key is not known within the dict, it will automatically be assigned the emptyset.
    freqTable = defaultdict(set)
    # Tokenizer used to split each sentence.
    tokenizer = RegexpTokenizer(r"\w+")
    # Get the current directory, including (of the current directory):
    # all subdirectories and all filenames,
    # os.walk ensures that the above is done recursively.
    for directory, subdirectory, filenames in walk(rootdir):
        for filename in filenames:
            # Skip both the script and the stored dict.
            if search(r"\.py$", filename) or search(r"\.pkl$", filename):
                continue
            # The file is an attachment.
            elif search(r"\.\d+\.txt$", filename):
                continue
            # The file a meta-data file.
            elif search(r"\_\d+\.xml$", filename):
                continue
            # The file is an email.
            else:
                with open(directory + "/"  + filename, mode='r', encoding='utf-8') as file:
                    # Filter out some (not all) unnecessary lines in the mail.
                    mail = filterMail(file.read())
                    # If the mail contains over 100.000 characters, it is probably faulty.
                    # Example: 3.163218.EGK2HGZCTFJ2VHQ2TTPV0TZZ2RX231X4B.txt
                    if(len(mail) > 100000):
                        continue
                    # Divide the filtered mail into somewhat logical sentences.
                    tokens = sent_tokenize(mail)
                    for token in tokens:
                        # Take the n-gram of each sentence.
                        for ngram in ngrams(tokenizer.tokenize(token), n):
                            # Add the frequency of the n-gram.
                            freqTable[ngram].add(filename)
    return freqTable
    
def filterMail(mail):
    mail = sub(r"(Message-ID:|Date:|From:|To:|Subject:).*?(\n\n)", "", mail, 0, VERBOSE | DOTALL | MULTILINE)
    return sub(r"\*\*\*\*\*\*\*\*\*.*\*\*\*\*\*\*\*\*\*", "", mail, 0, VERBOSE | DOTALL | MULTILINE)

def saveFreqTableToDisk(freqTable, filename):
    freqTableFile = open(filename + ".pkl", "wb")
    dump(freqTable, freqTableFile)
    freqTableFile.close()

if __name__ == '__main__':
    # Get the n to be used in the n-gram,
    # Get the directory from which that frequency table must be build,
    # Get the name of the output file.
    n, startDir, outputFile = init()
    # Start to build the frequency table.
    freqTable = buildFreqTable(n, startDir)
    # Store the frequency table to persistant storage.
    saveFreqTableToDisk(freqTable, outputFile)
