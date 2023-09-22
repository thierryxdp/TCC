def freq_palavras(frases):
    dicionario=dict()
    for x in str.split(frases):
        dicionario[x]= dicionario.get(x,0)+1
    return (dicionario)