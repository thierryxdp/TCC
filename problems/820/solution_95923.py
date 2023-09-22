def posLetra(frase,letra,num):
    if (num > frase.count(letra)):
        return -1
    i=0
    y=0
    x = frase.find(letra)
    while (i <= num):
        y += frase.find(letra,i)
        i += 1
        return x + y