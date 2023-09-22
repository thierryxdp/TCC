def posLetra(frase,letra,i): 
    if str.count(frase,letra) >= i and i > 1:
        return str.index(frase,letra,i)
    else:
        if i = 1:
            return str.index(frase,letra)
        else:
            return -1