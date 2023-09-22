def freq_palavras(frase):
    d={}
    x=frase.split()
    for e in x:
        y=x.count(e)
        d[e]=y
    return d