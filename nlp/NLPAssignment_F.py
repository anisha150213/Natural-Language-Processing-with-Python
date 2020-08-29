import nltk
from nltk import *


def write_file(list_word, file_name):
    f = open(file_name, 'w')
    text = '(pairs of two consecutive words, Frequency)'
    s1 = ''.join(str(text))
    f.write(str(s1))

    for i in list_word:
        s1 = ''.join(str(i))
        f.write('\n')
        f.write(s1)

    f.close()


# read dataset
BNC_file = open("Preprocessed_BNC.txt", "r")
CS_file = open("Preprocessed_CS.txt", "r")

# read stopwords file
stop_file = open('stopword.txt', 'r')
stop_words = stop_file.read()

# tokenize two files
BNC_words = word_tokenize(BNC_file.read())
CS_words = word_tokenize(CS_file.read())

# punctuations
filter_words = [' ', '?', '!', ',', ';', ':', '-', '--', '---',
                '(', ')', '{', '}', '[', ']', "'", '"', '.', '`', '·', '``', '~', "''"]

# remove punctuations
BNC_filtered_words = [w for w in BNC_words if w not in filter_words]
CS_filtered_words = [w for w in CS_words if w not in filter_words]

# remove stop words
BNC_Stop_filtered_words = [w for w in BNC_filtered_words if w not in stop_words]
CS_Stop_filtered_words = [w for w in CS_filtered_words if w not in stop_words]

# split into bigrams
BNC_bigrm = list(nltk.bigrams(BNC_Stop_filtered_words))
CS_bigrm = list(nltk.bigrams(CS_Stop_filtered_words))

# find most frequent bigrams for two datasets
BNC_frequency_Dist = FreqDist(BNC_bigrm)
BNC = BNC_frequency_Dist.most_common(100)

CS_frequency_Dist = FreqDist(CS_bigrm)
CS = CS_frequency_Dist.most_common(100)

write_file(BNC, 'F_bnc_output.txt')
write_file(CS, 'F_cs_output.txt')
