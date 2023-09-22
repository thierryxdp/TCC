def faltante (lista_elementos):
    
    list.sort(lista_elementos)
    i = 0
    
    while len(lista_elementos) > i :
        if lista_elementos[i] != (lista_elementos[i+1]-1):
            return i
        
        i +=1
        
    return i