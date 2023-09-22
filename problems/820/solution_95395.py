def posLetra(texto,letra,num):
    """..."""
    
    numero = str.count(texto,letra)
    
    if numero<num:
        return -1
    
    else:
        
        x = str.replace(texto,letra," ",num)
        indice = str.index(x,letra)
        return indice