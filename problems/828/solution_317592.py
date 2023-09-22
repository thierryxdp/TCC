def primo(n):
    '''função que dado um número inteiro positivo verifica
    se é primo ou não'''
    'int -> bool'
 
    if (n <= 3) : 
        return True
 
    if (n<=1 or n % 2 == 0 or n % 3 == 0) : 
        return False