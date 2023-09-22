def qtd_divisores(numero):
    """dado um numero de entrada, retorna a quantidade
    de divsores que esse número tem"""
    compilador=0
    listanumero=range(numero+1)
    for i in listanumero:
        if numero%i=0:
            compilador=compilador+1
    return compilador