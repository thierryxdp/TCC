def faltante (lista_elementos):
    
    if len(lista_elementos) ==  1:
        if lista_elementos[0] == 1:
            return 2
        else:
            return 1
            
    list.sort(lista_elementos)
    i = 0
    elemento_faltante = []
    
    while lista_elementos[i] == i+1:
        i +=1
    
    return lista_elementos[i] , i