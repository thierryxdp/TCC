def primo(n):
    """Função que informa se o número recebido é primo ou não.
    int -> bool """
    
    if n<=1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n//2 + 1):
            if n%i == 0:
                return False
    return True