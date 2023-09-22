def primo(n):
    '''funcao que dado um numero interiro positivo verifica
    se e primo ou nao'''
    'int -> bool'
    
    if(n <= 3) :
        return True
    
    if (n<=1 or n % 2 == 0 or n % 3 == 0):
        return False