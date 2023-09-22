def qtd_divisores(numero):
    """dado um numero de entrada, retorna a quantidade
    de divsores que esse número tem"""
    compilador=O
    for n in range(numero+1):
        if numero%n=0:
            compilador=compilador+1
    return compilador