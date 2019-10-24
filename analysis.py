import pandas as pd
from collections import Counter
import json
import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from nltk.stem.snowball import SnowballStemmer

docstring_tokens = ['Extracts', 'video', 'ID', 'from', 'URL', '.']
docstring = 'Extracts video ID from URL.'


#Definindo a linguagem de normalização
stemmer = SnowballStemmer('english')
nlp = spacy.load('en_core_web_sm')

#Função de normalização
def norma(text):
    text = nlp(text.lower())        
    termos = [token for token in text if not (token.is_stop or token.pos_ == 'PUNCT' or token.pos_ == 'PRON' or token.pos_ == 'CCONJ' or token.pos_ == 'DET')]
    texto = ''
    for term in termos:
        texto += ' ' + stemmer.stem(term.orth_) 
    return texto


norma(docstring)
print(docstring)
