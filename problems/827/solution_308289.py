def qtd_divisores(numero):
    """dado um numero de entrada, retorna a quantidade
    de divsores que esse número tem"""
    compilador=0
    for n in range(1,numero+1):
        if numero%n==0:
            compilador=compilador+1
    return compilador