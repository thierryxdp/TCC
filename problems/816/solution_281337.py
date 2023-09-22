def maiores(lista,n):
    '''Recebe uma lista de números inteiros e um número n e retorna uma lista com todos os 
    números inteiros maiores que n da lista original; lista, int -> lista'''
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    return lista[(a+1):]