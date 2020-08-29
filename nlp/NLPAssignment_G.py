import itertools

from nltk import BigramAssocMeasures, BigramCollocationFinder, word_tokenize, collocations


def write_file(list_word):
    for i in list_word:
        s1 = ''.join(str(i))
        f.write(s1)


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

bigram_measures = collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(BNC_Stop_filtered_words)

f = open('G_bnc_output.txt', 'w')
text = '\nChi-square Measure - '
s1 = ''.join(str(text))
f.write(str(s1))

bigrams = finder.nbest(bigram_measures.chi_sq, 20)
write_file(bigrams)

text = ' \nPMI Measure - '
s1 = ''.join(str(text))
f.write(str(s1))
bigrams = finder.nbest(bigram_measures.pmi, 20)
write_file(bigrams)

text = ' \nPhi-square Measure - '
s1 = ''.join(str(text))
f.write(str(s1))
bigrams = finder.nbest(bigram_measures.phi_sq,20)
write_file(bigrams)

text = ' \nDice Measure - '
s1 = ''.join(str(text))
f.write(str(s1))
bigrams = finder.nbest(bigram_measures.dice,20)
write_file(bigrams)

f.close()


finder = BigramCollocationFinder.from_words(CS_Stop_filtered_words)

f = open('G_cs_output.txt', 'w')
text = '\nChi-square Measure - '
s1 = ''.join(str(text))
f.write(str(s1))

bigrams = finder.nbest(bigram_measures.chi_sq, 20)
write_file(bigrams)

text = ' \nPMI Measure - '
s1 = ''.join(str(text))
f.write(str(s1))
bigrams = finder.nbest(bigram_measures.pmi, 20)
write_file(bigrams)

text = ' \nPhi-square Measure - '
s1 = ''.join(str(text))
f.write(str(s1))
bigrams = finder.nbest(bigram_measures.phi_sq,20)
write_file(bigrams)

text = ' \nDice Measure - '
s1 = ''.join(str(text))
f.write(str(s1))
bigrams = finder.nbest(bigram_measures.dice,20)
write_file(bigrams)

f.close()