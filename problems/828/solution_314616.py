def primo (n):
    '''verificar se o numero e primo ou nao'''
    if n < 2:
        return False

    for number in n.count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True