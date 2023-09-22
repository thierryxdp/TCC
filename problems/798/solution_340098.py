def freq_palavras(frases):
    freq=str.split(frases)
    dicionario={}
    for x in freq:
        if x in dicionario:
            dicionario[x]=dicionario[x]+1
        else:
            dicionario[x]=1
    return dicionario