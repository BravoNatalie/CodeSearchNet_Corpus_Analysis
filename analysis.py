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
arquivoEntrada = ["jsons.txt"]
parsed_json = []

#Definindo a linguagem de normalização
# stemmer = SnowballStemmer('english')
""" 
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
 """
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

def lerTokensDeArquivo(arqEntrada):
    linhas = []
    with open(arqEntrada) as f:
        for line in f:
            linhas.append(line.strip('\n'))
    f.close()
    return linhas

def splitLinhas(linhas):
    token_set = {}
    linha0 = str(linhas[0])
    split = linhas[0].split()
    qtdTokens = int(split[0])
    token_set['sc'] = []
    for x in range(1, len(split)):
        token_set[split[x]] = []
        #print(split[x])
    for x in range(1, len(linhas)):
        split = linhas[x].split()
        if(len(split) > 1):
            token_set[split[1]].append(split[0])
        else:
            token_set['sc'].append(split[0])
    return linha0, token_set
    
def writeMapAsLinestoFile(arquivoSaida, map):
    with open(arquivoSaida, 'w+') as o:
        o.write(linha0 + '\n')
        for k,v in map.items():
            if(str(k) == 'sc'):
                key = ''
            else:
                key = str(k)
            for entry in v:
                o.write(str(entry) + ' ' + key + '\n')
        o.close()

def writeMapAsJsonToFile(arquivoSaida, map):
     with open(arquivoSaida, 'w+') as o:
         o.write(json.dumps(map))
         o.close()

def sortAndWriteToFile(arqSaida, linhas):
    linhas.sort()
    with open(arqSaida, 'w+') as o:
        for l in linhas:
            o.write(l + '\n')
        o.close()

# conta as classificacoes diferentes
def contarDiferencas(linhas_vet):
    contDiferencas01 = 0
    contDiferencas02 = 0
    contDiferencas12 = 0
    tokens_dict = {}
    for i in range(0, len(linhas_vet)):
        for l in range(1, len(linhas_vet[i])):
            linha = linhas_vet[i][l]
            split = linha.split()
            if i == 0:
                tokens_dict[split[0]] = []
            if len(split) > 1:
                tokens_dict[split[0]].append(split[1])
            else:
                #print("Token sem classificacao:", split[0])
                tokens_dict[split[0]].append("sc")
            
    for k,v in tokens_dict.items():
        if v[0] != v[1]:
            contDiferencas01+=1
        if v[0] != v[2]:
            contDiferencas02+=1
        if v[1] != v[2]:
            contDiferencas12+=1
    print("Total de diferencas:")
    print("Entre Arqs 1 - 2:", contDiferencas01)
    print("Entre Arqs 1 - 3:", contDiferencas02)
    print("Entre Arqs 2 - 3:", contDiferencas12)

def numeroDeTokensPorCategoria(linhas):
    linha0, td = splitLinhas(linhas)
    for k,v in td.items():
        print(k, ":", len(v))

#norma(docstring)

#parseJson(arquivoEntrada, parsed_json)
#docstring2 = []
#for obj in parsed_json:
#processaTokens(obj["docstring_tokens"], tokens_proc)

#print(tokens_proc)
#print(len(tokens_proc))
#escreverTokensEmArquivo("tokens_processados.txt", tokens_proc)

linhas1 = lerTokensDeArquivo("tokens_class_alex.txt")
linhas2 = lerTokensDeArquivo("paraClassificar.txt")
linhas3 = lerTokensDeArquivo("tokens_class_natalie.txt")

numeroDeTokensPorCategoria(linhas3)

# Conta total de diferentes
vector = []
vector.append(linhas1)
vector.append(linhas2)
vector.append(linhas3)
contarDiferencas(vector)

#writeToFile("sortedList.txt",linhas1)


#linha0, token_map = splitLinhas(linhas1)
#writeMapAsLinestoFile("arq.txt", token_map)
#writeMapAsJsonToFile("tokens.json", token_map)







