def primo(num):
    """calculo e retorno de uma funçao que diz se um numero é primo ou não."""
    if num > 2:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
        else:
            return True