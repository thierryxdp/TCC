def filtra_pares(A):
    """ essa função ira filtrar somente numeros pares e ordenalos corretamente """
    return sorted(filter(lambda x: x % 2 == 0, A))