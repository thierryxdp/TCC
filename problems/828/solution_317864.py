def primo(n):
    ''' função que dado um numero inteiro positivo verifica
    se é primo ou não'''
    'int -> bool'
    
    if (n <=3):
        return True
    
    if (n<=1 or n % 2 == 0 or n % 3 == 0) :
        return False
    
    return True

    i = 5
    while(i* i<=n):
        if (n % i == 0 or n % (i + 2) == 0):
            return