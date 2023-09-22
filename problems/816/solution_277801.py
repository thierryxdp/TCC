def maiores(listan,n):
    '''retorna a lista com numeros maiores que 'n'. list,int->list'''
    listan.insert(0,n)
    list.sort(listan)
    a=listan.index(n)
    return listan[a+1:]