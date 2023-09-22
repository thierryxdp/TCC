def soma_h(n):
    '''Calcula o valor de H com n termos.
    int -> float'''
    h=1
    n=2
    for i in range(n-1):
        h=h+(1/n)
        n=n+1
    return round(h,2)