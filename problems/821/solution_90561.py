def fatorial(numero):
    """dado um numero inteiro de entrada retorna o fatorial dele
    int --> int"""
    contador=numero-1
    resultado=numero*contador
    while contador > 1:
        resultado=contador*resultado
        contador=contador-1
    return resultado