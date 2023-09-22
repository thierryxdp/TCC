def posLetra(frase,letra,num):
    if (num > frase.count(letra)):
        return -1
    elif ( num > 1 and num <= frase.count(letra)):
        frase = frase.replace(letra, ' ', num-1)
        return frase.index(letra)
    else:
        return frase.index(letra)