def qtd_divisores(num):
    ''' Essa função tem como objetivo verificar o total de divisores de
    um número'''
    '''int ->int'''
    contador = 0
    for d in range(1,num):
        if num%d == 0:
            contador += 1
    return contador