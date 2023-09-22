def fatorial(numero):
    """Calcula o fatorial de um número n; int->int"""
    fatorial=1
    while numero>0:
        fatorial=fatorial*numero
        numero=numero-1
    return fatorial