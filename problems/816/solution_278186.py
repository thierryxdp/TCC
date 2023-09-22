def maiores(inteiros,n):
    '''Retorna uma nova lista com os
       números inteiros maiores que n;
       list,int->list'''
    copia=inteiros
    inteiros+=[n]
    list.sort(inteiros)
    posicao=list.index(inteiros,n)
    return inteiros[posicao+1:]