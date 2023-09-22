def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=1
    par=n%2==0
    impar=n%2!=0
    while i < n:
        if n == par and n!=2:
            i+=1
        return False
        i+=1
        if n >= 2 and n == impar:
            i+=1
        return True
        i+-1