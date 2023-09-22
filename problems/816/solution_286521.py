def maiores(lista,n):
    '''
       Dada uma lista e um número n retorna uma nova lista
       apenas com os números maiores que n em ordem crescente
       list, int -> list
    '''
    if lista[0:-1] > n:
        list.append(lista)
        list.sort(lista)
        return lista