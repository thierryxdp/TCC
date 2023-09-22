def faltante(lista):
    
    list.sort(lista)
    
    conta_pecas = []
    i = 0
    acumulador = 1
    
    while i < len(lista):
        
        if lista[i] == acumulador:
            acumulador += 1
        
        i += 1
        
    return acumulador