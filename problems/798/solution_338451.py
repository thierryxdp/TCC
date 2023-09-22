def freq_palavras(frases):
    v={}
    frase=str.split(frases,' ')
    for x in frase:
        v[x]=list.count(frase,x)
    return v