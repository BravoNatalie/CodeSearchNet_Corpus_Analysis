# import pandas as pd
# from collections import Counter
import json
import spacy
# from spacy.lang.pt.stop_words import STOP_WORDS
# from nltk.stem.snowball import SnowballStemmer
from spacy.lang.en.stop_words import STOP_WORDS

docstring_tokens = ['Extracts', 'video', 'ID', 'from', 'URL', '.']
docstring = 'Extracts video ID from URL, over running run ran PALAVRA.'


#Define os arquivos de leitura
arquivoEntrada = ["selecionados.txt"]
parsed_json = []

#Definindo a linguagem de normalização
# stemmer = SnowballStemmer('english')

nlp = spacy.load('en_core_web_sm')

#adiciona stopwords customizadas
customSW = ['id']
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
def processaTokens(docstring, tokens_proc):
    docst = ''
    for entry in docstring:
        docst = docst + ' ' + entry
    tokens = nlp(docst)
    for token in tokens:
        tk = token.lemma_
        tk = tk.lower()
        if len(token) > 1 and token.is_stop==False and token.is_ascii and (token.pos_ == 'PROPN' or token.pos_ == 'NOUN') and tk not in tokens_proc:
            tokens_proc.append(tk)

def parseJson(arquivoEntrada, parsed_json):
    for arq in arquivoEntrada:
        with open(arq) as f:
            for line in f:
                parsed_json.append(json.loads(line))
            f.close()

def escreverTokensEmArquivo(arquivoSaida, tokens):
    with open(arquivoSaida, 'w+') as o:
        o.write(str(len(tokens)) + '\n')
        for token in tokens:
            o.write(token + '\n')
        o.close()


#norma(docstring)

parseJson(arquivoEntrada, parsed_json)
docstring2 = []
for obj in parsed_json:
    processaTokens(obj["docstring_tokens"], tokens_proc)

#print(tokens_proc)
#print(len(tokens_proc))
escreverTokensEmArquivo("tokens_processados.txt", tokens_proc)





