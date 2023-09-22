"""Recebe uma string e separa em um dicionario quantas vezes cada palavra aparece""""

def freq_palavras(frases):
    matue={}
    x= frases[0]
    for x in frases:
        if str.count(frases, x)==1:
            return matue+= {x: 1}
        if str.count(frases, x)==0:
            return matue
    return matue