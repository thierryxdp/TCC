def faltante (lista_elementos):
    
    if len(lista_elementos) ==  1:
        if lista_elementos[0] == 1:
            return 2
        else:
            return 1
        
    lista_falta1 = len(lista_elementos)-1
    list.sort(lista_elementos)
    i = 0
    while lista_elementos[i] >= i:
        i += 1
    return i