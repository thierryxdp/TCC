def freq_palavras(frase):
    d=dict()
    for i in frase:
        if i not in d:
            d[i]=1
        else: 
            d[i]+=1
    return d