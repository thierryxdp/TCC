def maiores(lista, n):
    """A função recebe uma lista de números inteiros e um inteiro
    n e retorna outra lista com os números da lista de entrada maiores
    que n, ordenados em ordem crescente."""
    nova_lista = []
    for elemento in lista:
        if elemento > n:
            nova_lista.append(elemento)
    
    list.sort(nova_lista)
    return nova_lista