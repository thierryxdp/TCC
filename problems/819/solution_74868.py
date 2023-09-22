def filtraMultiplos(lista_numeros,n):
    """dada uma lista de números e um número n, a função retorna outra lista, contendo os elementos da lista original que
    forem divisíveis por n; list, float -> list"""
    i = 0
    divisiveis = []
    while i < len(lista_numeros):
        if lista_numeros[i] % n == 0:
            divisiveis = divisiveis + [lista_numeros[i]]
        i = i + 1
    return divisiveis