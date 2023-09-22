def freq_palavras(frases):
    '''retorna um dicionário a partir da frase dada; str -> dict'''
    k = str.split(frases, ' ')
    d = {a:b}
    a = ''
    b = 0
    for i in k:
        a = a + k[i]
        b = b + 1
        d = d + {a:b}
        if k[i] in list(dict.values(d)):
            d = {a:b+1}
    return d