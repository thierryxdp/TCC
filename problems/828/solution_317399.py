def primo(n):
    '''
    Funçao que verifica se um numero é primo
    int-> bool
    '''
    if n == 2:
        return True
    elif n%(n**(1/2)) == 0:
        return False
    elif n%3 == 0 or n%5==0 or n%7==0:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            else:               
                return True