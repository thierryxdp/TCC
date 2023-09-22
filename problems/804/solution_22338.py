def filtra_pares (tupla):
    '''retorna uma nova tupla com os inteiros pares de uma tupla com 4 elementos inteiros de entrada
    tup -> tup'''
    tupla = ()
    filtro = []
    for x in tupla:
        if x%2==0:
            filtro.append(x)
    return tuple(filtro)