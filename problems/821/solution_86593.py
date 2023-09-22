def fatorial(numero):
    """Calcula o fatorial do numero.
    Entrada:int
    Saida:int"""
    contador=1
    acumulador=1
    while contador<=numero:
        acumulador=acumulador*contador
        contador=contador+1
    return acumulador