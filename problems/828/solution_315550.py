def primo(n):
    """Retorna true se n for primo e false caso não seja;
int -> bool"""
    for divisor in range(2,n):
        if n%divisor == 0:
            return False
        
    return True