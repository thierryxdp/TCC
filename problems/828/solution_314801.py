def qtd_divisores(numero):
    ''' dado um numero, retorna a quantidade de divisores desse
        numero.
        : int -> int
    '''
    divisores = 0
    for n in range(1,numero + 1):
        if numero%n == 0:
            divisores = divisores + 1
    return divisores

def primo (numero):
    '''
    '''
    if qtd_divisores(numero) != 2:
        return False
    else:
        return True