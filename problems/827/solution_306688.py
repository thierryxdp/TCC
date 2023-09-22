def qtd_divisores(numero):
    '''Função que, dado um número qualquer, retorna o número de divisores desse número.
int --> int'''
    qtd_divisores = 0
    for x in range(1,numero+1):
        if numero%x == 0:
            qtd_divisores = qtd_divisores + 1
    return qtd_divisores