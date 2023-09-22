def soma_h(N):
    '''função que calcula o valor de H dado um termo int(N),
    e retorna o valor de H com duas casas decimais;
    int->float'''
    resp=0
    for i in range(1,N+1):
        if N!=0:
            resp+=(1/i)
    return round(resp,2)