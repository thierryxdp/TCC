def posLetra(frase,letra,i): 
    if str.count(frase,letra) >= i:
        return str.index(frase,letra,i)
    else:
        return -1