def primo(numero):
    '''Verifica se um numero é inteiro positivo é primo ou não retornando um booleano
    para cada resultado.
    int -> bool'''
    divisores = []
    for i in range(1,numero+1):
        if numero % i == 0:
            divisores.append(numero)
    if len(divisores) == 2:
        return True
    else:
        return False