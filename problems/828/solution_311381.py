def primo(numero):
    '''dado um  número inteiro positivo, verifica se ele é primo ou não;
    int -> bool'''
    if numero == 2:
        return True
    for divisor in range(2,numero):
        if (numero%divisor) == 0:
            return False
    return True