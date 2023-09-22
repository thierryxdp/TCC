def primo(num):
    '''Dado um número inteiro positivo, verifique se este número é primo ou não.
    int->bool
    '''
    div=0
    for x in range(2,num):
        if num%x==0:
            div+=1
    if div==0:
        return True
    else:
        return False