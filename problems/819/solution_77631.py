def filtraMultiplos(lista,n):
    """recebe uma lista de números e retorna outra lista
    contendo os elementos que são divisíveis por n;
    list, int, -> list"""
    contar = 0
    caixa = []
    
    while contar < len(lista):
        if (lista[contar][0]) % n == 0:
            list.append(caixa, lista[contar])
        contar = contar + 1
    return caixa