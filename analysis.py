# import pandas as pd
# from collections import Counter
import json
import spacy
# from spacy.lang.pt.stop_words import STOP_WORDS
# from nltk.stem.snowball import SnowballStemmer
from spacy.lang.en.stop_words import STOP_WORDS

docstring_tokens = ['Extracts', 'video', 'ID', 'from', 'URL', '.']
docstring = 'Extracts video ID from URL, over running run ran PALAVRA.'


#Definindo a linguagem de normalização
# stemmer = SnowballStemmer('english')

nlp = spacy.load('en_core_web_sm')

#adiciona stopwords customizadas
customSW = ['over', 'id', 'palavra']
for token in customSW:
    STOP_WORDS.add(token)

#adiciona normalização
sbd = nlp.create_pipe('sentencizer')
nlp.add_pipe(sbd, first=True)

tokens_proc = []

#Função de normalização
def norma(text):
    text = nlp(text.lower())        
    termos = [token for token in text if not (token.is_stop or token.pos_ == 'PUNCT' or token.pos_ == 'PRON' or token.pos_ == 'CCONJ' or token.pos_ == 'DET')]
    texto = ''
    for term in termos:
        texto += ' ' + stemmer.stem(term.orth_) 
    return texto

#Remove stopwords, pontuação, normaliza verbos e remove duplicatas
def processaTokens(docstring):
    tokens = nlp(docstring)
    output = []
    for token in tokens:
        tk = token.lemma_
        if token.is_stop==False and token.pos_ != 'PUNCT' and tk not in output:
            output.append(tk)
    return output



#norma(docstring)
print(docstring)
tokens_proc = processaTokens(docstring)
print(tokens_proc)


