def primo(p):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    p = int
    
    for i in range(1,p+1):
        
        if p%i==0:
            return False 
        else: 
            True