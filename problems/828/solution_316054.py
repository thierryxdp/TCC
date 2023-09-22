def primo(num):
    '''retorna se o numero é primo ou nao,int->str'''
    i=0
    for numeros in range(2,num):
        if num % numeros == 0:
            i=i+1
    if i>0:
        return False
    else:
        return True