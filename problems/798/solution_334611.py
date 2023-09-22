def freq_palavras(frases):
    '''retorna um dicionário a partir da frase dada; str -> dict'''
    k = str.split(frases, ' ')
    d = {'ap':1}
    for i in range(len(k)):
        d[k[i]] = list.count(k, k[i])        
    del(d)['ap']
    return d