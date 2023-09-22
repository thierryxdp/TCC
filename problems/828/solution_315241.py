def primo(n):
    """Função que, dado um número inteiro (n), verifica se este número é primo ou não; int->booleano"""
    
    multiplos = 0
    
    for x in range(2,n):
        
        if (n % x == 0):
            
            multiplos += 1
            
    if(multiplos==0):
        
        return True
    
    else:
        
        return False