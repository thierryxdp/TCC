def freq_palavras(frases):
    frase = str.split(frases,' ')
    r={}
    for e in frase:
        r[e] = list.count(frase,e)
    return r