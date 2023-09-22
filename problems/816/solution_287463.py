def maiores (lista_numeros,n):
    '''retorna os elementos da lista maiores que n  em ordem crescente
    list, int --> list'''
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    pos_n=list.index(lista_numeros,n)
    lista_maiores=lista_numeros[pos_n+1:]
    list.sort(lista_maiores)
    return lista_maiores