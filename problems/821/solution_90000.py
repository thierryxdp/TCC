def fatorial(n):
    """dado um numero n de entrada
    retorna o fatorial desse numero
    int-->int"""
    multiplicador=n-1
    resultado=1
    while multiplicador>0:
        resultado2=n*multiplicador*resultado
        resultado=n*multiplicador
        multiplicador=multiplicador-1
        n=n-1
    return resultado