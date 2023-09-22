def freq_palavras(frase):
    frase= frase.split()
    dicio={}
    for palavra in frase:
        if palavra in dicio:
            dicio[palavra]+=1
        else:
            dicio[palavra]=1
    return dicio