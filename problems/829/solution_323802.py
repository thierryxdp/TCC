def soma_h(N):
    '''
    funcao que calcula e retorna o valor de H
    com N termos, sendo N dado de entrada
    int->float
    '''
    H=0
    for y in range(1,N+1):
        divisao=1/y
        H=H+divisao
    return round(H,2)