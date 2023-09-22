def primo(n):
    '''recebe e retorna True ou False se o número é primo
    int -> bool'''
    
    for i in range(2,n):
        
        if n % i == 0:
            return False
        
        else:
            return True