def faltante(lista):
    list.sort(lista)
    i=0
    
    while i < len(lista):
        if lista[i] - (lista[i]-1) != 1:
            return lista[i] - 1
        i += 1
        
    return