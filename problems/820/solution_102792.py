def posLetra(frase,letra,numero):
    
    if numero:
        return frase.index(letra,numero)
    elif frase.index(letra,numero)>numero:
        return -1