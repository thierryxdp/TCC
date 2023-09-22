def faltante(lista):
    
    Q = len(lista)
    i = 0
    
    while i <= Q-2:
        if lista[i] == lista[i+1] -1:
            i = i + 1
        
        return lista[i+1] -1
        
    return lista[-1]