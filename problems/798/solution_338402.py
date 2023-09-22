# Coloque um comentário dizendo o que a função faz
def freq_palavras(frases):
    palavras=str.split(frases,' ')
    dicionario={}
    for i in palavras:
        dicionario[i]=list.count(i,palavras)
    return dicionario