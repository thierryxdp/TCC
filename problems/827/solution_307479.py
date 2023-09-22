def qtd_divisores(numero):
    '''Retorna a quantidade de
    divisores do numero inserido
    int --> int'''
    qntd = 0
    for i in range (1,numero+1):
        if numero % i == 0:
            qntd = qntd + 1
    return qntd