def fatorial(numero):
    """dado um numero inteiro de entrada retorna o fatorial dele
    int --> int"""
    if numero==1 or numero==0:
        return 1
    else:
        contador=numero-2
    imediato=numero-1
    resultado=numero*imediato
    while contador > 0:
        resultado=contador*resultado
        contador=contador-1
    return resultado