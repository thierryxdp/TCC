def faltante (L):
    
    if 1 not in L:
        return 1
    
    contador = 1
    if contador == len (L):
        return contador
    
    while contador < len (L):
        if contador not in L:
            return contador
        contador += 1
    return L [contador - 1] + 1