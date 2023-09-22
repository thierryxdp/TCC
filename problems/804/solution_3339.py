def filtra_pares(tupla):
    '''Funcao que recebe uma tupla com quatro elementos inteiros e retorna
    uma nova tupla apenas com os elementos pares da tupla original;
    tupla -> tupla'''
    pares = []
    for elemento in tupla:
        if elemento%2==0:
            pares.append(elemento)
    return tuple(pares)