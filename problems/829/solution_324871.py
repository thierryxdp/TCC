def soma_h(numero):
    """funcao que calcula o valor de h"""
    h=0
    for n in range(1,numero+1):
        h= 1/(n)
    return (round(h,2))