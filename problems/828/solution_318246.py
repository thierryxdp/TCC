def primo(n):
    '''a funçaõ verifica se o numero n é primo ou não
    int->bool'''
    primos=0
    for i in range(1,n+1):
        if n%i==0:
            primos+=1
    if primos==2:
        return True
    else:
        return false