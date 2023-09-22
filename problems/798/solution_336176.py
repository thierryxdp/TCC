def freq_palavras(frases):
    '''Uma função que recebe uma frasa e numera as
    palavras por quantidade str --> dict(str:int)'''
    d = dict()
    for palavras in frases[0].split(" "):
        if palavras in d:
            d[palavras] += 1
        else:
            d[palavras] = 1
    return d