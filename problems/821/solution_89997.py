def fatorial(n):
    """dado um numero n de entrada
    retorna o fatorial desse numero
    int-->int"""
    multiplicador=n-1
    resultado=0
    while multiplicador>0:
        resultado=n*multiplicador+resultado
        multiplicador=multiplicador-1
    return resultado