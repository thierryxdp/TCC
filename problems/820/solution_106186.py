def posLetra(frase,letra,i): 
    if str.count(frase,letra) >= i and i > 1:
        return str.index(frase,letra,i)
    else:
        return -1