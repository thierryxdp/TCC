def soma_h(n):
    """essa função recebe um número n e retorna o valor de H com n termos;
    int->float"""
    h = 0
    for i in range(1,n+1):
        h += 1/i
    return round(h,2)