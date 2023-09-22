def maiores (lista,n):
    """Insira uma lista e um numero inteiro, a funcao ira retornar outra lista contendo
    numeros da lista originais maiores que n, em ordem crescente"""
    maiores = list()
    lista.sort()
    for x in lista:
        if x>=n:
            maiores.append(x)
    return maiores