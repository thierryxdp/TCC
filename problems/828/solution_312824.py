def primo(n):
    '''Funcao que dado um numero inteiro positivo, verifica se o mesmo e primo ou nao'''
    '''int -> bool'''
    for i in range (1, n):
        if n % i == 0 and i <= n and i >= 2:
            return True
        else:
            return False