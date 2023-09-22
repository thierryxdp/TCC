# Coloque um comentário dizendo o que a função faz
def freq_palavras(frases):
    palavras=str.split(frases,' ')
    dicionario={}
    contador=0
    for i in palavras:
        dicionario+=dict(i=list.count(frases,i))
    return dicionario