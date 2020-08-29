from nltk import FreqDist
from nltk.tokenize import word_tokenize


def write_file(text, number):
    write_word = text + number
    f.write(write_word)
    f.write('\n')


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
BNC_filtered_sentance = [w for w in BNC_words if w not in filter_words]
CS_filtered_sentance = [w for w in CS_words if w not in filter_words]

BNC_TWords = len(BNC_filtered_sentance)
CS_TWords = len(CS_filtered_sentance)

# computing frequency for two dataset
BNC_frequency_Dist = FreqDist(BNC_filtered_sentance)
CS_frequency_Dist = FreqDist(CS_filtered_sentance)

BNC = BNC_frequency_Dist.most_common()
CS = CS_frequency_Dist.most_common()

BNC_length = len(BNC)
CS_length = len(CS)


f = open('D_total_output.txt', 'w')
write_file('BNC Total Words = ', str(BNC_TWords))
write_file('CS Total Words = ', str(CS_TWords))
write_file('BNC Unique Words = ', str(BNC_length))
write_file('CS Unique Words = ', str(CS_length))
write_file('BNC Type/Token ratio = ', str(BNC_length/BNC_TWords))
write_file('CS Type/Token ratio = ', str(CS_length/CS_TWords))
write_file('Total Type/Token ratio = ', str(((BNC_length+CS_length)/(BNC_TWords+CS_TWords))))
f.close()
