def primo(n):
    '''funçao que dada um numero inteiro positivo verifica se o mesmo é primo ou não usando um valor booleano int -> bool'''
    num_primo = 0
    
    for i in range (1 , 1 + n):
        
        if n % i ==0:
            
            num_primo += 1
           
    if num_primo == 2:
        
        return True
    
    else:
        
        return False