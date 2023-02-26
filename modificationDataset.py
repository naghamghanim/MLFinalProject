import pandas as pd
import itertools
import numpy as np
import linecache

#df = pd.read_csv('/content/Corpus.csv',encoding='utf8')
#df2 = pd.DataFrame(df, columns = ['token', 'flat_tag'])
#df2.to_csv('/content/Corpus2.csv',sep=' ', index=False,encoding='utf8')

file1 = open('/var/home/nhamad/NERproject/AllData.csv', 'r')
train = open("/var/home/nhamad/NERproject/data/train.txt", 'w')
test = open("/var/home/nhamad/NERproject/data/test.txt", 'w')

Lines = file1.readlines()


# Strips the newline character
for line in Lines[:449825]:
    train.write(line) 

test.write("RowID,corpus_name,sentence_id,word_id,global_sentence_id,token,flat_tag")
test.write('\n')
for line in Lines[449825:]:
    test.write(line)