def filtraMultiplos (lista, n):
    '''função que retorna k números inteiros divisiveis por n,
    sendo k E R; list, int -> list'''
    i = 0
    acumulador = []
    while i < len(lista):
        i = i + 1
        if lista [i] % n == 0:
            acumulador = acumulador + [lista[i]]
            return acumulador