def primo(n):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    
    for i in range(3,10):
        if n%i == 0:
            return False
        if n%2 == 0:
            return False
        if n% 2 != 0:
            return True