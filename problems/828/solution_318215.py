def primo(n):
    '''retorna se o número é primo ou não;
int->bool'''

    d=2

    for valor in range(2,n):
        if n%d==0:
            d=d+1
            return False

        else:
            d=d+1
        
    return True