def qtd_divisores(n):
    ''' conta quantos divisores um número n tem;
    int/float -> int '''
    d=0
    for elem in range(1,n+1):
        if n%elem==0:
            d = d+1
    return d