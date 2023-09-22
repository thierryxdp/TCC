def primo(n):
    '''função que dado um número inteito irá identificar se
    o número é ou não um número primo e retornará um boolenado True caos seja primo
    int->bool'''
    for i in range(2,n):
        if n%i==0 :
            return False
            n=n+1
    return True