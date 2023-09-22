def fatorial(numero):
    """dado um numero inteiro de entrada retorna o fatorial dele
    int --> int"""
    contador=numero-1
    resultado=1
    while contador > 0:
        resultado=numero*contador*resultado
        contador=contador-1
    return resultado