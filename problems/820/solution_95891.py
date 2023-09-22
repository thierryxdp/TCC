def posLetra(frase,letra,num):
    if (num > frase.count(letra)):
        return -1
    i=1
    x=frase.index(letra)
    while (i<=num):
        novafrase=frase[frase.index(letra)+1:]
        i=i+1
        return novafrase