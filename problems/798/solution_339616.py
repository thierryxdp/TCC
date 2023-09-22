def freq_palavras(frases):
    d={}
    for e in frases.split(' '):
        d[e]=dict.get(d,e,0)+1
    return d