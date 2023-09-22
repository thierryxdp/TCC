def primo(n):
    '''função que dado um número inteiro positivo verifica
    se é primo ou não'''
    'int -> bool'
 
     if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    
    
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = x
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + x+1
 
    return True