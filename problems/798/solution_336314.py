def freq_palavras(frases):
    """ REcebe uma string e retorn um dicionário contendo 
    a palavra e seu respectivo número de repeticoes na string
    str->dict"""
    for palavra in frases:
        if palavra in frases:
        	repeticoes=str.count(frases,palavra)
            dicio={}
       		dicio[palavra]=repeticoes
    return dicio