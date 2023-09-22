def faltante (lista):
    """Recebe uma lista de números de tamanho N - 1, ou seja,
    com menos valores que esperado, com os valores indo de 
    1 a N. Retorna o número faltando nas listas.
    list -> int"""
    list.sort (lista)
    indice = 1
    resultado = 0
    if 1 not in lista:
        return 1
    elif lista[-1] < len(lista) + 1:
        return len(lista) + 1
    while indice < len(lista):
        if lista[indice] - lista[indice-1] > 1:
            resultado += lista[indice] + 1
        indice += 1
    return resultado