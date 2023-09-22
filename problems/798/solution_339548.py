def freq_palavras(frase):
    pal=frase.split()
    dicio={}
    for i in range(len(pal)):
        dicio[pal[i]]=pal.count(pal[i])
    return dicio