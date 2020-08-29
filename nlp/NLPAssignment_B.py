from operator import itemgetter

from nltk import FreqDist
from nltk.tokenize import word_tokenize


def find_range_word(list_word):
    word_list = []
    word_frequency = []

    for i in range(100, len(list_word), 1):
        word_list.append(list_word[i])
        word_frequency.append(list_word[i][1])

    unique_frequency = sorted(set(word_frequency), reverse= True)

    final = []

    for i in unique_frequency:
        temp_list = []
        for j in word_list:
            if i == j[1]:
                temp_list.append(j)
        final.append(sorted(temp_list, key=itemgetter(0), reverse= True))

    return final


def print_list_word(list_word, file_name):
    count = 0
    word_lst = []
    f = open(file_name, 'w')
    for i in list_word:
        for j in i:
            if count == 1000:
                s1 = ''.join(word_lst)
                f.write(s1)
                f.write('\n')
                count = 0
                word_lst = []

            else:
                count += 1
                word_lst.append(str(j))
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

BNC = BNC_frequency_Dist.most_common()
CS = CS_frequency_Dist.most_common()


BNC_final_list = find_range_word(BNC)
CS_final_list = find_range_word(CS)

print_list_word(BNC_final_list, 'B_bnc_output.txt')
print_list_word(CS_final_list, 'B_cs_output.txt')



