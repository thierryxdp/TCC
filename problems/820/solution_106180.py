def posLetra(frase,letra,i): 
    while str.count(frase,letra) > i:
        return frase.index(letra,i)