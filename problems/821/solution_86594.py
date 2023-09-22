def fatorial(numero):
    """funcao que dado um numero calcule seu fatorial.
    int->int"""
    i=1
    x=list(range(numero+1))
    while i<len(x):
        y=x[i]*x[i+1]
        i=i+1
    return y