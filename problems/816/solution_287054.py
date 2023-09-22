def maiores(l,n):
    '''Retorna uma lista com todos os números de l maiores que n
    list -> list'''
    for x in l:
        if x<=n:
            l.remove(x)
    if n not in l:
        l.append(n)
        list.sort(l,reverse=True)
        if n==l[0]:
            list.clear(l)
        else:
            l.remove(n)
            
    list.sort(l, reverse=False)
    return l