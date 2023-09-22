def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=1
    par=n%2==0
    while i < n:
        if n >= 2 and n%i!=0 and n%1==0 and n%n==0 and  n%i!=par:
            i+=1
            return False
        else:
            return True