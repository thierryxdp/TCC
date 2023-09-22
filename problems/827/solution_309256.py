def qtd_divisores(n):
    '''
    funcao que conta quantos divisores um
    determinado numero n tem
    int->int
    '''
    div=0
    for y in range(1,n+1):
        if n%y==0:
            div=div+1
    return div