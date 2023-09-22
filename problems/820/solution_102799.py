def posLetra(frase,letra,numero):
    if frase.index(letra)< numero:
        return frase.index(letra)
    
    if numero==1:
        return frase.index(letra)
    
    elif frase.index(letra)>0:
        return -1