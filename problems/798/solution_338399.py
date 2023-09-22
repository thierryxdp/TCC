# Coloque um comentário dizendo o que a função faz
def freq_palavras(frases):
    palavras=str.split(frases,' ')
    dicionario={}
    for i in palavras:
        x=list.count(i,palavras)
        dicionario[[i]=x]
    return dicionario