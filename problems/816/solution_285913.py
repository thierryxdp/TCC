def maiores(lista,n):
    ''' Essa função recebe uma lista de números inteiros e um números inteiro n,
    e retorna outra lista que contém todos os números da primeira lista maiores
    que n e ordenados de forma crescente;
    list,int->list'''
    l = lista
    list.append(l,n)
    list.sort(l)
    lista_nova = l[list.index(l,n)+1]
    return lista_nova