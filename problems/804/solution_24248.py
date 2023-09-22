def filtrapares(tupla):
    '''Essa função é fornecida com um grupo de 4 números e retorna somente os pares
    str, str, str, str -> str'''
    lista_tupla = []
    for elemento in T:
        if elemento%2==0:
            lista_tupla.append(elemento)
    return tuple(lista_tupla)