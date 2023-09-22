def fatorial(numero):
    """Função que, dado um número, retorne seu fatorial
    entrada: int
    saída:int"""
    fatorial=1
    while numero!=1:
        fatorial=fatorial*numero
        numero=numero-1
    return fatorial