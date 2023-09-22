def primo(p):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    for i in range(2,p):
        if p%i == 0:
            return False