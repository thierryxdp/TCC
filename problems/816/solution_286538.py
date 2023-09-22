def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um numero intero n retorna uma outra lista que contenha todos os numeros da lista original maiores que n;
    list, int -> list'''
    l1 = list.append(lista,n)
    list.sort()
    l2 = l1[n:]
    return l2