def posLetra(frase,letra,num):
    if (num > frase.count(letra)):
        return -1
    i=0
    while (i<num):
        x=frase.index(letra)
        novafrase=frase[frase.index(letra)+1:]
        i=i+1
        return novafrase