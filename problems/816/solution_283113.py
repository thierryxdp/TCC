def maiores(lista,n):
    """recebe uma lista de numeros inteiros e um numero n e retorna todods os numeros
da lista maiores que n.
lista,int->lista"""
    list.sort(lista)
    return lista[n:]