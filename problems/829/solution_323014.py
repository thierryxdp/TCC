def soma_h(n):
    '''retorna o valor de H com n termos;
    int->float'''
    H=1
    for x in range(2,n+1):
        H=H+1/x
    return round(H,2)