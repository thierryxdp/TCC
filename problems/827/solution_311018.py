def qtd_divisores(numero):
    '''retorna a quantidade de divisores que um numero possui; int -> int'''
    divisores = []
    x = 1
    while x <= numero:
        if numero%x == 0:
            divisores = divisores + [x,]
        x = x + 1
    return len(divisores)