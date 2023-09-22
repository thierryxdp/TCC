def primo(numero):
    '''funcao que indica se o numero de entrada é um numero primo o nao. O
    numero de entrada deve ser positivo.
    int -> bool'''
    divisores = 0
    for divisor in list(range(1,4):
        if numero % divisor == 0:
            divisores += 1
    if divisores == 1:
        return True
    else:
        return False