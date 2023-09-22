def filtra_pares(tupla):
    """Função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla apenas com os elementos pares da tupla original.
    Use tupla: (elemento1,elemento2,elemento3,elemento4).
    tupla -> tupla"""
    pares = []
    for elemento in tupla:
        if elemento%2==0:
            pares.append(elemento)
    return tuple(pares)