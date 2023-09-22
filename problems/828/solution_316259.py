def primo(numero):
    '''função que diz se um número é primo ou não
    True= número primo; False= número não primo
    valor de entrada: int
    valor de saída: bool'''
    for divisores in range(2,numero):
        if divisores%numero == 0:
            return False
        else:
            return True