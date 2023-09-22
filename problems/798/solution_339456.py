def freq_palavras(frases):
    """Retorna um dicionário com as palavras de uma frase e seu respectivo número de aparições.
    str->dic"""
    d=dict()
    frases1=str.split(frases,' ')
    for c in frases1:
        if c not in d:
            d[c]=0
        if c in d:
            d[c]+=1
    return d