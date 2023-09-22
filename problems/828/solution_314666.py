def primo (n):
    '''retorna se é um número(n) é primo(true) ou não(false)'''
    if n > 1:
        for i in range(2, n//2):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False