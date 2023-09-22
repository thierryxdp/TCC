def qtd_divisores(numero):
    """dado um numero de entrada, retorna a quantidade
    de divsores que esse número tem"""
    compilador=O
    listanumero=range(numero+1)
    for n in listanumero:
        if numero%n=0:
            compilador=compilador+1
    return compilador