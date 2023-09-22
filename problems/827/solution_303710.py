def qtd_divisores(x):
    '''Função que dado um número x de entrada calcula quantos divisores este número possui.
    int->int'''
    qntd = 0
    for i in range(1,x+1):
        if x % i == 0:
            qntd += 1
    return qntd