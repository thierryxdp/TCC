def freq_palavras(frases):
    p = frases.split(' ')
    d={}
    for i in p:
        d[i]=p.count(i)
    return d[i]