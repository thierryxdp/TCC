def freq_palavras(frases):
    """ REcebe uma string e retorn um dicionário contendo 
    a palavra e seu respectivo número de repeticoes na string
    str->dict"""
    str.strip(frases,',')
    str.strip(frases,'.')
    sentence=str.split(frases)
    for palavra in frases:
        dicio={}
        repeticoes=str.count(frases,palavra)
        dicio[palavra]=repeticoes
    return dicio