def maiores(lista_inteiros, n):
    """funcao que recebe uma lista de numero inteiros e um numero n qualquer e retorna uma lista de numero inteiros e ordenados maiores que n.
    list, int -> list"""
    lista_inteiros.append(n)
    lista_inteiros.sort()
    lista_inteiros = lista_inteiros[lista_inteiros.index(n) +1:]
    return lista_inteiros