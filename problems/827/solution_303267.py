def qtd_divisores(n):
    '''Retorna quantos divisores o número n possui;
    int -> int'''
    div=0
    for i in range(1,n+1):
        if n%i==0:
            div=div+1
    return div