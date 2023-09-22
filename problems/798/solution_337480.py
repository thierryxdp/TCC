def freq_palavras(frases):
    dicio={}
    frase=str.split(frases)
    i=0
    for i in range(len(frase)+1):
        repetido=list.count(frases,frase[i])
        dicio[frase[i]]=repetido
        i=i+1
    return dicio