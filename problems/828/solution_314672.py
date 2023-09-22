def primo(numero):
    '''funcao que indica se o numero de entrada é um numero primo o nao. O
    numero de entrada deve ser positivo.
    int -> bool'''
    divisores = 0
    for divisor in list(range(2,numero+1)):
        resto = numero%divisor
        if resto == 0 and divisor!=numero:
            return False
        else:
            return True