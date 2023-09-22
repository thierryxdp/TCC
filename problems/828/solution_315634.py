def primo(num):
    '''Dado um número inteiro positivo, verifique se este número é primo ou não.
    int->bool
    '''
    div=0
    for x in range(1,num+1):
        if num%x==0:
            div+=1
    if div==2:
        return True
    else:
        return False