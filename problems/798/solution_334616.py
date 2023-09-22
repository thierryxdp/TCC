def freq_palavras(frases):
    '''retorna um dicionário a partir da frase dada; str -> dict'''
    k = str.split(frases, ' ')
    d = {'samara':10}
    for i in range(len(k)):
        d[k[i]] = list.count(k, k[i])        
    del(d)['samara']
    return d