def filtra_pares(T):
    '''Essa função, quando fornecida com um grupo de 4 números, retorna somente os pares'''
    lista_T = []
    for n in T:
        if n%2 == 0:
            lista_T.append(n)
    return tuple(lista_T)