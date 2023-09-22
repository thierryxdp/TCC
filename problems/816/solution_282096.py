def maiores(list,n):
    '''Dada uma lista de números inteiros e um numero 
    inteiro n, retorna uma lista com os elementos da lista 
    original que forem maiores que n; list , int -> list'''
    
    list.append(list,n)
    list.sort(list)
    ind_n = list.index(list,n)
    return list[ind_n+1:]