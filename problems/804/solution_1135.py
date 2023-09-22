def filtra_pares(a,b,c,d):
    """filtra os números pares de uma lista"""
    lista1 = [a,b,c,d]
    return filter(lista1%2==0,lista1)