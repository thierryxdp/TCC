def posLetra(texto,letra,num):
    """..."""
    
    numero = str.count(frase,letra)
    
    if numero<num:
        return -1
    
    else:
        
        x = str.replace(frase,letra," ",num)
        indice = str.index(x,letra)
        return indice