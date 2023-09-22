def freq_palavras(frases):
    dicio={}
    frase=str.split(frases)
    i=0
    while i <len(frase):
        repetido=list.count(frase,frase[i])
        dicio[frase[i]]=repetido
        i=i+1
    return dicio