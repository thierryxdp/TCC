def faltante(lista_int: list)-> int:
    
    list.sort(lista_int)
    num_faltante = list()
    i = 0
    
    while(( lista_int[i] + 1 == lista_int[i + 1]) and i < len(lista_int) - 1):
        i += 1
        
    num_faltante[0] = lista_int[i] + 1
        
    return num_faltante[0]