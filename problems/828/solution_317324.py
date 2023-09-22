def primo(numero):
    '''função que recebe um inteiro positivo e
    verifica se ele é primo ou não
    int -> bool
    '''
    for n in range(2,numero +1):
        if numero%n == 0:
            return False
        else:
            return True