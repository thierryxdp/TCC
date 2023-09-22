def freq_palavras (frases):
    d={}
    for p in str.split(frases):
        if p in d:
            d[p] +=1
        else:
            d[p]=1
    return d