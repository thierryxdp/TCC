def primo(n):
    '''Retorna se o número n é primo ou não'''
    '''int->bool'''
    divisores=0
    for x in range(1,n+1):
        if n%x==0:
            divisores=divisores+1
    if divisores>2:
        return False
    elif n==1:
        return False
    else:
        return True