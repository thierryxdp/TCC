def primo(n):
    '''recebe e retorna True ou False se o número é primo
    int -> bool'''
    
    div = 0
    
    for i in range(2,n):
        if n % i == 0:
            div = div + 1
            
            
    if div == 0:
        return True
    else:
        return False