def qtd_divisores(n):
    '''conta a quantidade de divisores que um número n tem;
    int -> int'''
    div = 0 
    for x in range (n+1):
        z = n%x
        if z== 0 :
        	div = div + x
    return div