def qtd_divisores(numero):
    ''' dado um numero calcula e retorna o numero de divisoes'''
    divisores = ()
    for x in range(1,numero+1):
        if numero%x == 0:
            divisores = divisores + (x,)
    return len(divisores)