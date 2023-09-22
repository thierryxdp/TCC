def primo(p):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    divisores = 0
    
    for i in range(1, p):
        if p % i == 0:
            divisores = divisores + 1
            
        if divisores > 1:
            return False
        
    else:
        return True