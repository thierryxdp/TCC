def soma_h(n):
    """funcao que calcula a expressao.
    int->float"""
    soma=0
    for x in range(1,n+1):
        y=1/x
        soma=soma+y
    return round(soma,2)