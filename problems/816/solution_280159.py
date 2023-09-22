def maiores(lista,n):
    """ Essa função retorna os números inteiros da lista
    maiores do que n. lista,int-> lista"""
    lista.append(n)
    lista.sort(reverse = True)
    return lista