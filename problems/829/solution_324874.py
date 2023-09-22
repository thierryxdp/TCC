def soma_h(numero):
    """funcao que calcula o valor de h"""
    h=0
    for n in range(numero):
        h += 1/(n+1)
    return (round(h,2))