def maiores(inteiros,n):
    '''Retorna uma nova lista com os
       números inteiros maiores que n;
       list,int->list'''
    ultimo=inteiros[-1]
    inteiros=range(n+1,ultimo+1)
    return list(inteiros)