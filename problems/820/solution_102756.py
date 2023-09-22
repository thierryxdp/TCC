def posLetra(frase,letra,numero):
   
    if frase.index(letra)<numero :
        return frase.index(letra,numero)
    elif frase.index(letra)==1:
        return frase.index(letra,numero)
    elif frase.index(letra)>numero:
        return -1