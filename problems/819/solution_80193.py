def filtraMultiplos (lista, n):
    '''função que retorna k números inteiros divisiveis por n,
    sendo k E R; list, int -> list'''
    i = 0
    acumulador = []
    while i < len(lista):
        if lista[i] % n == 0:
            i = i + 1
            acumulador = acumulador +  [lista[i]]
            return acumulador