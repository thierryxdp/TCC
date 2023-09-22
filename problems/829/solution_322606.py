def soma_h(n):
    '''
    recebe um inteiro n e retorna 1+(1/2)+(1/3)+...+(1/n)
    int->float
    '''
    h=1
    for i in range(2,n+1):
        h=h+(1/i)
    return h