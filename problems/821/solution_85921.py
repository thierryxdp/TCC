def fatorial (x):
    """Função que calcula o fatorial de dado numero x
        int -> float"""
    contador=1
    fat=1
    acumulador=[]
    while contador<=x:
        fat=fat*contador
        acumulador=acumulador+[fat]
        contador=contador+1
        
    return acumulador[-1]