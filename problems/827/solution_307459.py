def qtd_divisores(numero):
    num_div = 0
    for x in range(1,numero+1):
        if numero%x == 0:
            num_div = num_div + 1
    return num_div

def primo2(numero):
    '''função que, dado um número conta quantos divisores
    um certo numero tem e retorna a quantidade de divisores
    int ->int'''
    num_div = 0
    for x in range(1,numero+1):
        if numero%x == 0:
            num_div = num_div + 1
    if num_div == 2:
        return True
    else:
        return False