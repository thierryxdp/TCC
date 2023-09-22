def maiores(lista,n):
    '''Dada uma lista de números inteiros e um numero 
    inteiro n, retorna uma lista com os elementos da lista 
    original que forem maiores que n; list , int -> list'''
    
    list.append(lista,n)
    list.sort(lista)
    ind_n = list.index(lista,n)
    n_repetido = list.count(lista,n)
    return lista[ind_n+n_repetido:]