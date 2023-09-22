def primo(numero):
    '''função que recebe um inteiro positivo e
    verifica se ele é primo ou não
    int -> bool
    '''
    divisor = 0
    for n in range(2,numero):
        if numero%n == 0:
            divisor += 1
    if divisor == 0:
        return True
    else:
        return False