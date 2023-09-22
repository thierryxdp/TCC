def maiores (lista, n):
    '''funcao que, dada uma lista de numeros inteiros e um numero inteiron, retorna uma nova lista com todos os elementos da lista dada maiores do que o elemento n
    lista, int -> lista'''
    lista = [n]+lista
    list.sort(lista)
    list.index(lista,n) + list.count(lista,n)
    lista2 = lista[n:]
    return lista2