def maiores(numeros,n):
    """a função ordena a lista, encontra o indice do número e retorna os valores maiores.
    Entradas lista, int e saida lista"""
    list.sort(numeros)
    x = list.index(numeros,n)
    return numeros[x+1:]