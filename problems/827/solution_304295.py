def qtd_divisores(numero):
    '''funçao que conta qnts divisores um numero tem'''
    divisores = 0
    for c in range(1,numero+1):
        if numero%c == 0:
            divisores +=1
        else:
            pass
    return divisores