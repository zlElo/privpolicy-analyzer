import json
import re
from analyse.summarzation_de import *
from analyse.summarzation_en import *

# keywords language
language_german = ['ist', 'ja', 'sein', 'und', 'der', 'das', 'nein', 'ein', 'zu']
language_english = ['is', 'yes', 'no', 'the', 'his', 'new', 'and', 'a', 'to']


def detect_lang(file):

    with open(f'data/{file}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    first_key = next(iter(data))  # get the first key from the JSON object
    text = data[first_key]

    for word in language_german:
        if re.search(r"\b" + re.escape(word) + r"\b", text):
            print(f'detect german with following word: {word}')
            language = 'de'
            summ_de(file)


    for word_ in language_english:
        if re.search(r"\b" + re.escape(word_) + r"\b", text):
            print(f'detect english with following word: {word_}')
            language = 'en'
            summ_en(file)
    
    print('\r')
