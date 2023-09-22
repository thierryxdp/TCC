def filtra_pares(lista):
    """filtra apenas os números pares de uma lista"""
    A = (list(lista)[0])%2==0
    B = (list(lista)[1])%2==0
    C = (list(lista)[2])%2==0
    D = (list(lista)[3])%2==0
    if A and B and C and D:
        return list(lista)
    if A and B and C:
        return list(lista[0:3])