def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=2
    while x % i != 0 and i <= x/2:
        i=i+1
    if x % i == 0:
        return False
    else:
        return True