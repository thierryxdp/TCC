def fatorial(numero):
    """Dado um número qualquer, retorna a fatorial do numero:
    int-->int"""
    i=numero
    while i>1:
        i-=1
        numero=numero*i
    return numero