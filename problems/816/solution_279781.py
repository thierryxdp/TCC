def maiores(list,n):
    '''função que dada uma lista e um numero inteiro n,retorna outra lista que
    contenha todos od números da lista maiores que n
    list,int->list'''
    list.append(n)
    list.sort()
    pos_n=list.index(n)
    return list[pos_n+1:]