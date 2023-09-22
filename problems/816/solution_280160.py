def maiores(lista,n):
    """ Essa função retorna os números inteiros da lista
    maiores do que n. lista,int-> lista"""
    lista.append(n)
    lista1 = list.sort(lista)
    if lista1[:] > n:
        return lista1[<n]