def faltante(lista_int: list)-> int:
    
    list.sort(lista_int)
    num_faltante = list()
    i = 0
    
    while( i < len(lista_int)):
        if (lista_int[i] + 1 == lista_int[i + 1]):
            i += 1
        else:
            num_faltante[0] = lista_int[i] + 1
            
    return num_faltante[0]