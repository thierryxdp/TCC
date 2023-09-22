def freq_palavras(frases):
    """ REcebe uma string e retorn um dicionário contendo 
    a palavra e seu respectivo número de repeticoes na string
    str->dict"""
    sentence=str.split(frases)
    for palavra in sentence:
        dicio:{}
        if palavra in frases:
        repeticoes=str.count(frases,palavra)
        dicio[palavra]=repeticoes
    return dicio