def filtraMultiplos(lista,n):
    '''
       Funcao que recebe uma lista de numeros e um numero,
       retornando uma lista com numeros divisiveis por n.
       list,int -> list
    '''
    multiplos = []
    m = 0
    
    while m < len(lista):
        if lista[m] %n == 0:
            multiplos.insert(m,lista[m])
            m = m + 1

    return multiplos