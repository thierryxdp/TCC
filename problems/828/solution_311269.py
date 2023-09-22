def primo(n):
    '''Dado um número n retorna se ele é ou não primo
    int -> bol'''
        for i in range(2, int(n / 2) + 1):
                if n % i == 0:
                        return False
        return True