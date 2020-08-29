from nltk import FreqDist
from nltk.tokenize import word_tokenize


def write_file(word_list, unique_frequency, file_name):
    f = open(file_name, 'w')
    text = '(No of words , Frequency)'
    s1 = ''.join(str(text))
    f.write(str(s1))
    for i in unique_frequency:
        count = 0
        for j in word_list:
            if i == j[1]:
                count = count + 1
        text = count, i
        s1 = ''.join(str(text))
        f.write('\n')
        f.write(str(s1))
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

# frequency list for datasets
BNC_frequency_list = []
for i in BNC:
    BNC_frequency_list.append(i[1])

CS_frequency_list = []
for i in CS:
    CS_frequency_list.append(i[1])


# Sort and unique frequency list
BNC_unique_frequency = sorted(set(BNC_frequency_list))
CS_unique_frequency = sorted(set(CS_frequency_list))

write_file(BNC, BNC_unique_frequency, 'C_bnc_output.txt')
write_file(CS, CS_unique_frequency, 'C_cs_output.txt')
