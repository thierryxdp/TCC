def freq_palavras(frases):
    '''retorna um dicionário a partir da frase dada; str -> dict'''
    k = str.split(frases, ' ')
    d ={:}
    for i in frases:
        d[frases[i]] = str.count(k, frases[i])
    return d