def freq_palavras(frase):

    i=0
    dicio={}
    separar=str.split(frase)
    for freq in separar:
        freq=separar.count(separar[i])
        dicio[separar[i]]=freq
             
    return dicio