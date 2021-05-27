from os import walk, path
from collections import defaultdict 
from re import sub, search, VERBOSE, DOTALL, MULTILINE
from nltk import sent_tokenize, word_tokenize, ngrams, RegexpTokenizer
from pickle import dump
 
def buildFreqTable(rootdir, n):
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

def saveFreqTableToDisk(freqTable):
    freqTableFile = open("frequency_table.pkl", "wb")
    dump(freqTable, freqTableFile)
    freqTableFile.close()

if __name__ == '__main__':
    # Get the current directory in which the script is executed.
    # All files in this directory and subsequent subdirectories,
    # will be used to construct the frequency table.
    currentdir = path.dirname(path.abspath(__file__))
    freqTable = buildFreqTable(currentdir, n=4)
    saveFreqTableToDisk(freqTable)
