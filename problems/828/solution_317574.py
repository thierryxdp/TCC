def primo(numero):
    '''
    função que recebe um número como parâmetro e retorna
    um booleano afirmando se ele é primo ou não
    int -> bool
    '''
    if numero < 2:
        return False
    else:
        for n in range(2, numero):
            if numero % n == 0:
                return False
        return True