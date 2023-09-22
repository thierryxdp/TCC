def fatorial (x):
    """Função que calcula o fatorial de dado numero x
        int -> float"""
    contador=1
    fat=1
    while contador<=x:
        fat=fat*contador
        contador=contador+1
        
    return fat