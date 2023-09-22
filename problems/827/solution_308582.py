def qtd_divisores(num):
    ''' Essa função tem como objetivo verificar o total de divisores de
    um número'''
    '''int ->int'''
    d=0
    contador = 0
    while d != 0:
        if num%d == 0:
            contador += 1
        d+1
    return contador