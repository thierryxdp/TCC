def posLetra(frase,letra,num):
    if (num > frase.count(letra)):
        return -1
    i=1
    x=frase.index(letra)
    y=0
    while (i<=num):
        frase=frase[frase.index(letra)+1:]
        y += frase.find(letra)
        i=i+1
    return y + x + 1