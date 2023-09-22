def freq_palavras(frases):
    d=dict()
    frases==frases.split('')
    for i in frases:
        if i not in d:
            d[i]=1
        else:
                d[i]+=1
    return d