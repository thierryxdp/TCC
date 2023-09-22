def fatorial(numero):
    """funcao que dado um numero calcule seu fatorial.
    int->int"""
    i=1
    x=list(range(numero+1))
    y=0
    while i<len(x):
        y=y*x[i]
        i=i+1
    return y