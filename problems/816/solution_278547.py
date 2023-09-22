def maiores(lista, n):
    """Dada uma lista de números inteiros e um número inteiro n, retorna
    outra lista com todos os números maiores que n"""
    list.append(lista,n)
    ordenada = sorted(lista)
    indice = list.index(ordenada,n)
    if n not in ordenada:
        list.append(lista,n)

    return ordenada[indice+1:]