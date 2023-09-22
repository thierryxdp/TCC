def freq_palavras(frases):
    '''retorna um dicionário a partir da frase dada; str -> dict'''
    k = str.split(frases, ' ')
    d = {'a':1}
    for i in frases:
        d[frases[int(i)]] = str.count(k, frases[int(i)])
    del(d)['a']
    return d