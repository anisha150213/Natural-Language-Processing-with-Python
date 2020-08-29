import unidecode as unidecode
from bs4 import BeautifulSoup
import re
from string import digits


# remove html tags
def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text(separator=" ")
    return stripped_text


# remove extra white space
def remove_extra_white_space(text):
    res = (re.sub(' +', ' ', text))
    return res


# remove accented characters : café
def remove_accented_chars(text):
    text = unidecode.unidecode(text)
    return text

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


# remove special characters
def remove_special_characters(text):
    return re.sub('[!,*)@#<>|+-=~`/%(&$_?.^]', '', text)


# convert all to lower case
def convert_lower_case(text):
    return str.lower(text)


# convert number to numeric : two to 2
def text2int(textnum, numwords={}):
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ""
    onnumber = False
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                if onnumber:
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
            else:
                scale, increment = numwords[word]

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True

    if onnumber:
        curstring += repr(result + current)

    return curstring


# remove numbers
def remove_digits(text):
    remove_digit = str.maketrans('', '', digits)
    return text.translate(remove_digit)


BNC_file = open("bnc.txt", "r")
BNC_words = BNC_file.read()

remove_html_tag = strip_html_tags(BNC_words)

remove_extra_space = remove_extra_white_space(remove_html_tag)

remove_accent_char = remove_accented_chars(remove_extra_space)

word_contraction = decontracted(remove_accent_char)

remove_special_char = remove_special_characters(word_contraction)

lower_case = convert_lower_case(remove_special_char)

convert_n2m = text2int(lower_case)

remove_number = remove_digits(convert_n2m)


f = open("Preprocessed_BNC.txt", "w")
f.write(remove_number)
f.close()


CS_file = open("cs.txt", "r")
CS_words = CS_file.read()

remove_html_tag = strip_html_tags(CS_words)

remove_extra_space = remove_extra_white_space(remove_html_tag)

remove_accent_char = remove_accented_chars(remove_extra_space)

word_contraction = decontracted(remove_accent_char)

remove_special_char = remove_special_characters(word_contraction)

lower_case = convert_lower_case(remove_special_char)

convert_n2m = text2int(lower_case)

remove_number = remove_digits(convert_n2m)

f = open("Preprocessed_CS.txt", "w")
f.write(remove_number)
f.close()
