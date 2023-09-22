def posLetra(x,y,z):
    """Função que retorna em que posição a ocorrência estava
        str,str,int->int"""
    i = 0
    ocor = 0
    a = str.count(x,y)
    
    if a < z:
        return -1
    
    while ocor < z:
        if y[i] == x
           ocor += 1
        i += 1
    return i-1