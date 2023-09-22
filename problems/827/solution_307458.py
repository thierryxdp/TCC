def qtd_divisores(numero):
    '''Função que, dado um número qualquer, retorna o 
    número de divisores desse número.
    int --> int'''
    num_div = 0
    for x in range(1,numero+1):
        if numero%x == 0:
            num_div = num_div + 1
    return num_div

def primo2(numero):
    num_div = 0
    for x in range(1,numero+1):
        if numero%x == 0:
            num_div = num_div + 1
    if num_div == 2:
        return True
    else:
        return False