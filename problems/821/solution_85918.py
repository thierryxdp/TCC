def fatorial (x):
    """Função que calcula o fatorial de dado numero x
        int -> float"""
    contador=0
    acumulador=[]
    fat=1
    while contador<x:
        fat=fat*contador
        acumulador=acumulador+[fat]
        contador=contador+1
    return acumulador