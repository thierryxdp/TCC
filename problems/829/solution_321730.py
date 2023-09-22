def soma_h(n):
    '''Calcula o valor de H com n termos.
    int -> float'''
    h=1
    x=2
    for i in range(n-1):
        h=h+(1/n)
        x=x+1
    return round(h,2)