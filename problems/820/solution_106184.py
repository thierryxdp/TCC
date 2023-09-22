def posLetra(frase,letra,i): 
    if str.count(frase,letra) >= i:
        return frase.index(letra,i)
    else:
        return -1