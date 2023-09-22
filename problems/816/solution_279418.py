def maiores(L,n):
    '''Recebe uma lista de numeros inteiros e um numero n e retorna outra 
    lista que contenha todos os numeros da lista original maiores que n;
    list,int -> list'''
    list.append(L,n)
    list.sort(L)
    x=list.index(L,n)
    return L[x+1:]