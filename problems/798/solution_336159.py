def freq_palavras(frases):
    '''Uma função que recebe uma frasa e numera as
    palavras por quantidade str --> dict(str:int)'''
    d = dict()
    for c in frases:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d