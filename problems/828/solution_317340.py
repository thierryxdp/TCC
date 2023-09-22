def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=1
    while n % i != 0 and i <= n/2:
        i=i+1
    if n % i == 0:
        return False
    else:
        return True