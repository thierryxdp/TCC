def qtd_divisores(n):
    '''Dado um numero(n), calcula quantos divisores o numero possui.int->int'''
    i=0
    j=1
    k=0
    if n<=0:
        return 0       
    while i<n:
        if n%j==0:
            k=k+1
            j=j+1
        else:
            j=j+1
        i=i+1
    return k