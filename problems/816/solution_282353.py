def maiores(lista,n):
    """Funcao que retorna os numeros de uma lista maiores que n 
    ordenados de forma crescente
    entrada: list, int
    saida: list"""
    x = lista + [n]
    list.sort(x)
    z = list.index(x,n)
    del x[:z+1]
    return x