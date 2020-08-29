from nltk import FreqDist
from nltk.tokenize import word_tokenize


def write_file(list_word, file_name):
    print(len(list_word))
    f = open(file_name, 'w')
    for i in list_word:
        s1 = ''.join(str(i))
        f.write(s1)
        f.write('\n')

    f.close()


# Read input files
BNC_file = open("Preprocessed_BNC.txt", "r")
CS_file = open("Preprocessed_CS.txt", "r")


# tokenize two files
BNC_words = word_tokenize(BNC_file.read())
CS_words = word_tokenize(CS_file.read())

# filter words to remove punctuation
filter_words = [' ', '?', '!', ',', ';', ':', '-', '--', '---',
                '(', ')', '{', '}', '[', ']', "'", '"', '.', '`', '·', '``', '~', "''"]

# Filtered two datasets to remove punctuations
BNC_filtered_word = [w for w in BNC_words if w not in filter_words]
CS_filtered_word = [w for w in CS_words if w not in filter_words]

# computing frequency for two dataset
BNC_frequency_Dist = FreqDist(BNC_filtered_word)
CS_frequency_Dist = FreqDist(CS_filtered_word)

BNC = BNC_frequency_Dist.most_common(100)
CS = CS_frequency_Dist.most_common(100)

# file write
write_file(BNC, 'A_bnc_output.txt')
write_file(CS, 'A_cs_output.txt')
