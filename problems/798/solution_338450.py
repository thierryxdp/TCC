def freq_palavras(frases):
    v={}
    frase=str.split(frases,' ')
    for x in frases:
        v[x]=list.count(frase,x)
    return v