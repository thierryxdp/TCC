def faltante (lista_elementos):
    
    if len(lista_elementos) ==  1:
        if lista_elementos[0] == 1:
            return 2
        else:
            return 1
            
    list.sort(lista_elementos)
    i = 0
    
    while len(lista_elementos) > i :
        if lista_elementos[i] == lista_elementos[i+2]-1:
        else:
            return i +1 
        i +=1
        
    return none