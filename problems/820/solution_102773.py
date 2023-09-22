def posLetra(frase,letra,numero):
   
    if frase.index(letra)<numero:
        return frase.index(letra,numero)
    elif numero==1:
        return frase.index(letra,numero)
    elif frase.index(letra,numero)>numero:
        return -1
    elif numero==1
        return 0