def qtd_divisores(numero):
    '''retorna quantos divisores o numero inserido tem.
    int -> int'''
    divisores = ()
    for i in range(1, numero+1):
        if numero / i == numero // i:
            divisores = divisores + (i,)
    return len(divisores)