def qtd_divisores(n):
    '''Função que, dado um número, calcula seu número de divisores.
    int --> int'''
    quantidade = 0
    for numero in range(1,(n+1)):
        if n%numero == 0:
            quantidade = quantidade + 1
    return quantidade