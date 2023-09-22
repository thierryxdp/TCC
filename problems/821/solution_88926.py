def fatorial(numero):
    """Funcao que dado um numero, calcula o seu fatorial;
    int -> int"""
    acumulador=[]
    while numero>1:
        acumulador=[numero]*numero
        numero-=1
    return sum(acumulador)