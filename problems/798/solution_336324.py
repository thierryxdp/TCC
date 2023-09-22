def freq_palavras(frases):
    """ REcebe uma string e retorn um dicionário contendo 
    a palavra e seu respectivo número de repeticoes na string
    str->dict"""
    dicio={}
    sentence= str.split(frases)
    for palavra in sentence:
        rep=list.count(frases,sentence)
       	dicio[palavra]=rep
    return dicio