def filtraMultiplos(lista_numeros, num):
    '''
    Funcao que recebe uma lista de numeros e um numero n. A funcao retorna outra lista contendo todos os elementos
    da lista origial que forem divisiveis por n.
    list, int -> list
    '''
    con = 0
    nova_lista = []
    while (con<len(lista_numeros)):
        if lista_numeros[con]%num == 0:
            nova_lista.append(lista_numeros[con])
        con = con+1
    return nova_lista