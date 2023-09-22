def faltante(lista_int: list)-> int:
    
    list.sort(lista_int)
    num_faltante = 0
    
    i = 0
    
    while(i < len(lista_int) - 2):
        
        if (lista_int[i] + 1 != lista_int[i+1]):
            num_faltante = lista_int[i] + 1

        i += 1

    return num_faltante