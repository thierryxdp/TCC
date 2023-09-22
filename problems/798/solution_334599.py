def freq_palavras(frases):
    '''retorna um dicionário a partir da frase dada; str -> dict'''
    k = str.split(frases, ' ')
    d = {'a':1}
    i = 0
    while i < len(k):
        d[frases[i]] = str.count(k, frases[i])
        i = i + 1
    del(d)['a']
    return d