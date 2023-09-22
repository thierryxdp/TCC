def primo(p):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    if numero>1:
        for p in range(2,numero):
            if p%numero == 0:
                return True