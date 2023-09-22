def freq_palavras(frase):
    d=dict()
    frase=frase.split(' ')
    for i in frase:
        if i not in d:
            d[i]=1
        else: 
            d[i]+=1
    return d