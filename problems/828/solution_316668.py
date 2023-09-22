def primo(p):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    if p == 1 or p == 2 or p == 3 or p == 5 or p == 7:
        return True
    
    for i in range(3,10):
        if p%i == 0:
            return False
        if p%2 == 0:
            return False