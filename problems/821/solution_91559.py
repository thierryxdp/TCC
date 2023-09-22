def fatorial(x):
    """funcao que dado um numero, calcula o seu fatorial
int->int"""
    i = 1
    fatorial = 1
    while i<=x:
        fatorial = fatorial*i
        i = i+1
    return fatorial