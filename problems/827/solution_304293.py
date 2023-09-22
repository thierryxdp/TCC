def qtd_divisores(numero):
    '''funçao que conta qnts divisores um numero tem'''
    divisores = []
    for c in range(1,numero+1):
        if numero%c == 0:
            divisores.append(c)
        else:
            pass
    return divisores