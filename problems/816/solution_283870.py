def maiores (lista,n):
    """ Função que, dadas uma lista de números inteiros e um número inteiro n, 
    retorna uma lista com todos os números maiores do que o n dado em ordem crescente
    list, int->list"""
    list.insert(lista,0,n)
    list.sort(lista)
    del lista [0:(list.index(lista,n)+list.count(lista,n))]
    return lista