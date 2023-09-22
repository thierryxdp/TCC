def filtra_pares(a, b, c, d):
    """ essa função ira filtrar somente numeros pares e ordenalos corretamente """
    lista1=[a,b,c,d]
    return sorted(filter(lambda x: x % 2 == 0, lista1))