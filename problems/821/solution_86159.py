def fatorial(numero):
    """Funcao que recebe um numero e retorna seu fatorial"""
    n=(numero-1)
    multiplicacao=numero*n
    if numero==1:
        return 1
    else:
        while n>1:
            n=n-1
            multiplicacao=multiplicacao*n
        return multiplicacao