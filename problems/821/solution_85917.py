def fatorial(x):
    """Função que dado um numero x ,calcula o fatorial desse numero
        int -> float"""
    soma=0
    fat=1
    i=1
    while i<x+1:
        fat=fat*i
        i+1
    return fat