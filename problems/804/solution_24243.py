def filtrapares(T):
    '''Essa função é fornecida com um grupo de 4 números e retorna somente os pares
    str, str, str, str -> str'''
    lista_T = []
    for n in T:
        if n%2 == 0:
            lista_T.append(n)
    return tuple(lista_T)