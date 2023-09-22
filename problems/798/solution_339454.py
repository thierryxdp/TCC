def freq_palavras(frases):
    d=dict()
    frases1=str.split(frases,' ')
    for c in frases1:
        if c not in d:
            d[c]=0
        if c in d:
            d[i]+=1
    return d