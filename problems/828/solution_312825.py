def primo(n):
    '''Funcao que dado um numero inteiro positivo, verifica se o mesmo e primo ou nao'''
    '''int -> bool'''
    i = 2
    while i <= math.sqrt(n):
        if n % i < 1:
            return False
        i += 1
    return n > 1