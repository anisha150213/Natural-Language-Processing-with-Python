from nltk import FreqDist
from nltk.tokenize import word_tokenize


def write_file(list_word, file_name):
    f = open(file_name, 'w')
    for i in list_word:
        s1 = ''.join(str(i))
        f.write(s1)
        f.write('\n')

    f.close()


# Read input files
BNC_file = open("Preprocessed_BNC.txt", "r")
CS_file = open("Preprocessed_CS.txt", "r")
stop_file = open('stopword.txt', 'r')

stop_words = str.lower(stop_file.read())

# tokenize two files
BNC_words = word_tokenize(BNC_file.read())
CS_words = word_tokenize(CS_file.read())


# filter words to remove punctuation
filter_words = [' ', '?', '!', ',', ';', ':', '-', '--', '---',
                '(', ')', '{', '}', '[', ']', "'", '"', '.', '`', '·', '``', '~', "''"]

# Filtered two datasets to remove punctuations
BNC_filtered_word = [w for w in BNC_words if w not in filter_words]
CS_filtered_word = [w for w in CS_words if w not in filter_words]


BNC_Stop_filtered_word = [w for w in BNC_filtered_word if w not in stop_words]
CS_Stop_filtered_word = [w for w in CS_filtered_word if w not in stop_words]
# computing frequency for two dataset
BNC_frequency_Dist = FreqDist(BNC_Stop_filtered_word)
CS_frequency_Dist = FreqDist(CS_Stop_filtered_word)

BNC = BNC_frequency_Dist.most_common(100)
CS = CS_frequency_Dist.most_common(100)

write_file(BNC, 'E_bnc_output.txt')
write_file(CS, 'E_cs_output.txt')
