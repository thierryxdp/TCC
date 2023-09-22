def maiores(lista,n):
    """Dada uma lista de números inteiros e um número inteiro
    n retorna na lista apenas os números maiores do que n.
    list,int-> list"""
    lista2 = [elem for elem in lista if elem > n]
    lista2.sort(reverse = False)
    return lista2