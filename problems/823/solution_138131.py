def faltante (lista_elementos):
    
    if len(lista_elementos) ==  1:
        if lista_elementos[0] == 1:
            return 2
        else:
            return 1
        
    lista_completa = len(lista_elementos)+1
    list.sort(lista_elementos)
    i = 0
    
    if lista_completa != lista_elementos[i] :
        i +=1 
        
    return i