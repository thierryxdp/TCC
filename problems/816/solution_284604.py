def maiores (lista_numeros,n):
    '''retorna os elementos da lista maiores que n  em ordem crescente
    list, int --> list'''
    list.sort(lista_numeros)
    lista_maiores=lista_numeros[list.index(lista_numeros,n)+1:]
    list.sort(lista_maiores)
    return lista_maiores