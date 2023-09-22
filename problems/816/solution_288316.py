def maiores(lista, n):
    """Função que retorna dada uma lista e um número inteiro n retorna outra lista.
    list, int -> int"""
    maiores_numeros = []
    for numeros in lista:
        if numeros >= n:
            maiores_numeros.append(numeros)
    return maiores_numeros
sorted(maiores_numeros)