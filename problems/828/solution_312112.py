def primo(n):
    '''dado um numero inteiro maior que zero como entrada, retornando true caso o mesmo seja um número primo e false se não for
    int->bool'''
    x=0
    for i in range(2,n):
        if (n%i==0):
            x+=1
    if (x==0):
        return True
    else:
        return False