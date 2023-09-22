def maiores(lista,n):
    """Dada uma lista de números inteiros e um número inteiro
    n retorna na lista apenas os números maiores do que n.
    list,int-> list"""
    lista1 = list.sort(lista,n)
    lista2 = [elem for elem in lista1 if elem > n]
    return lista2