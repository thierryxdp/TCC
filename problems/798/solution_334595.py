def freq_palavras(frases):
    '''retorna um dicionário a partir da frase dada; str -> dict'''
    k = str.split(frases, ' ')
    d = {'a':1}
    for i in k:
        d[frases[i]] = str.count(k, frases[i])
    del(d)['a']
    return d