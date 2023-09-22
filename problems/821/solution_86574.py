def fatorial(numero):
    """esta função recebe um número e retorna o fatorial dele
    int-> int"""
    a=1
    while numero>0:
        a=a*numero
        numero=numero-1
    return a