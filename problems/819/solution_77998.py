def filtraMultiplos(Lista, n):
    '''Função que retorna os multiplos de n
    lis, int -> lis'''
    
    lc = len(Lista)
    i = 0
    lista = []

    while i < lc:
        if not Lista[i] %n:
            list.append(lista, Lista[i])
        i += 1
    return lista