def maiores(l,n):
    '''Retorna uma lista com todos os números da lista l original maiores que n
    list , int -> list'''
    for x in l:
        if x<=n:
            list.remove(l,x)
        l.remove(reverse=False)
        
        return l