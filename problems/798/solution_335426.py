def freq_palavras(frase):
    d={}
    for c in frase:
        if c in not d:
            d[c]=1
        else:
            d[c]+= 1
     return d