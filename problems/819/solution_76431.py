def filtraMultiplos(lista, numero):
    '''Funcao que filtra os multiplos de um numero e retorna uma lista com eles.
    list, int -> list'''
    
    i = 0
    listaMultiplos = []
    
    while i < len(lista):
        if lista[i] % numero == 0:
            list.append(listaMultiplos, lista[i])
    
    return listaMultiplos