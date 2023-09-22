def fatorial(numero):
    """Funcao que dado um numero, calcula o seu fatorial;
    int -> int"""
    acumulador=[]
    contador=numero
    while contador>1:
        acumulador=[contador]*contador
        contador=contador-1
    return sum(acumulador)