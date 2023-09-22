def filtraMultiplos(numeros, divisor):
    """Função que, dada uma lista de números e um número,
    retorna outra lista contendo todos os elementos da lista
    original que forem divisíveis por n.
    list, int -> list"""
    lista = []
    i = 0
    while i < len(numeros):
        if numeros[i] % divisor == 0:
            lista.extend(numeros[i])
        i = i + 1
    return lista