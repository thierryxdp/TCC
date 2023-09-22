def maiores(lista_numeros, n):
    """Função que recebe uma lista de numeros inteiros e um numero inteiro n,
    retornando outra lista, contendo os numeros inteiros maiores que n
    entrada: lista, int
    retorno: lista"""
    lista=list()
    for elemento in lista_numeros:
        if elemento > n:
            lista.append(elemento)
    lista.sort()
    return lista