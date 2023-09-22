def freq_palavras(frases):
    lista=frases.split()
    dicio={}
    n=0
    for x in lista:
        dicio[x]=lista.count(x)
    return(dicio)