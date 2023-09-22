def primo(p):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    if numero != 0 and numero != 1:
        if numero > 3:
            for i in range(2, numero):
                if numero % i == 0:
                    return False