freq_palavras(frases):
    dicionario={}
    i=0
    frase= str.split(frases,)
    while i< len(frases):
        a=list.count(frase, frase[i])
        dicionario[frase[i]=a
    return dicionario