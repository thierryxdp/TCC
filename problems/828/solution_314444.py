def primo(n):
    '''Retorna se o número é primo.
    int -> bool'''
    acc = 0
    for i in range(0, n + 1):
        if n % i == 0:
            acc += 1
    if acc >= 2:
        return False
    return True