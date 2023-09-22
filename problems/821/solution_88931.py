def fatorial(numero):
    """Funcao que dado um numero de entrada,
    retorne seu fatorial;
    int -> int"""
    contador=numero
    acumulador=[]
    indice=0
    resultado=0
    while contador>0:
        acumulador+=numero
        contador=contador-1
    while indice<len(acumulador):
        resultado*=acumulador[0]*acumulador[indice+1]
        indice+=2
    return resultado