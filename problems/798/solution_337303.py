def freq_palavras(frases):
    dicio={}
    frase=str.split(frases)
    i=0
    for i in range(len(frase)):
        repetido=str.count(frases,frase[i])
        dicio[frase[i]]=repetido
    return dicio