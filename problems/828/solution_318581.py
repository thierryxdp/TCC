def primo(x):
    '''retorna true se um numero inteiro de entrada x for primo, e false se nao for
    int -> bool'''
    for i in range(2, x):
        if x % i == 0:
            return False
        if not x % i == 0:
            return True
        if x <= 1:
            return False