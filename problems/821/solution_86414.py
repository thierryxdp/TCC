def fatorial(x):
    """calculo e retorno do fatorial de um numero"""
    if x==1:
        return 1
    else:
        return x * fatorial(x-1)