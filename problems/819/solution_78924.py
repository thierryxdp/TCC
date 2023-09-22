def filtraMultiplos(lista, n):
    '''Função que filtra os múltiplos de n contidos na lista de entrada.
    list, int -> list'''
    
    lista2 = []
    
    for m in lista:
        if (m%n) == 0:
            lista2 = lista2 + [m]
            
    return lista2