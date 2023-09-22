def maiores(lista,n):
    ''' Essa função recebe uma lista de números inteiros e um números inteiro n,
    e retorna outra lista que contém todos os números da primeira lista maiores
    que n e ordenados de forma crescente;
    list,int->list'''
    list.append(lista,n)
    list.sort(lista)
    lista_nova = lista[list.index(lista,n)+1:]
    return lista_nova