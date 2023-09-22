def primo(n):
    '''retorna se o número é primo ou não;
int->bool'''


    for d in range(2,n):
        if n%d==0:
            return False

        else:
            d=d+1
        
    return True