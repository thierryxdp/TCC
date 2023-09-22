def primo(n):
    '''Uma função dado um inteiro retornar se é primo ou não
    int -> booleano'''
if n != 0 & n != 1:
        if n > 3:
            for i in range(2, n):
                if n % i == 0:
                    return False
        return True
    return False