def posLetra(frase,letra,numero):
    if frase.index(letra)< numero:
        return frase.index(letra,numero)
    
    elif frase.index(letra,numero)>0:
        return -1