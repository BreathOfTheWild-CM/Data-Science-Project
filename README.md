# Data-Science-Project

import pandas as pd
import re
import glob
import os
# for all the files in all the folders in /vol/tensusers/fvheerwaarden/enron/data
sentences = []
direcs = glob.glob('/vol/tensusers/fvheerwaarden/enron/data/*/text_000/') 
for direc in direcs:
  for root, dirs, files in os.walk(direc):
    for file in files: ## this should walk trough our emails, but it can probably be done more efficient.
      file = open('test_freq.txt', 'r').read()
      pattern = '\.\s|\n|\?|!'
      list_file = re.split(pattern, file) # splits the file into sentences, assuming sentences end with a period and a whitespace. ?, ! and endlines (\n) are also recognized. Some whitespaces end up in the list.
sentences.extend(list_file)
df_sentences = pd.DataFrame(sentences, columns = ['Sentences'])
freq_table = pd.crosstab(index = df_sentences['Sentences'], columns = 'frequency') ##makes a frequency table, case sensitive
freq_table = freq_table.sort_values(by = ['frequency'], ascending = False)
print(freq_table)
freq_table.to_csv('output.csv')
