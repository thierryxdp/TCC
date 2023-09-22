def freq_palavras(frases):
    """ REcebe uma string e retorn um dicionário contendo 
    a palavra e seu respectivo número de repeticoes na string
    str->dict"""
    dicio={}
    sentence= str.slit(frases)
    for palavra in sentence:
        rep=str.count(frases,palavra)
       	dicio[palavra]=rep
    return dicio