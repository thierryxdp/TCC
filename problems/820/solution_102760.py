def posLetra(frase,letra,numero):
   
    if numero==1:
        return frase.index(letra,numero)
    elif frase.index(letra)>numero:
        return -1