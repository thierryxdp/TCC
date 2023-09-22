def maiores(inteiros,n):
    '''Retorna uma nova lista com os
       números inteiros maiores que n;
       list,int->list'''
    inteiros+=[n]
    list.sort(inteiros)
    list.sort(inteiros[n:])
    return inteiros