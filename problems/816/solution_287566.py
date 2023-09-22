def maiores(lista,n):
    """Retorna os valores maiores que n de uma lista de numeros;lista,int=>lista"""
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]