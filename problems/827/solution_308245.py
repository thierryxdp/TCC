def qtd_divisores(entrada):
    '''Dado um númeor inteiro, retorna quantos divisores esse número tem.
    int-->int'''
    qtd=0
    for n in range(1,entrada+1):
        if entrada%n==0:
            qtd=qtd+1
    return qtd