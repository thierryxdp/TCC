def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=1
    while i <= n:
        if n%i==0:
            i+=1
            return True