def maiores(lista,n):
    '''função que recebe como entrada uma lista de numeros inteiros, e um número
inteiro "n", retornando uma outra lista contendo todos os numeros inteiros da lista
original maiores que "n", em ordem crescente; list,int->list'''

    list.append(lista,n)
    list.sort(lista)
    indice=list.index(lista,n)
    lista2=lista[indice+1:]

    return lista2