def primo(x):
    """
    dado um número, verifica se o mesmo é primo
    """
    
    for i in range(x-1):
        if x%(i+1)==0 and i>=1:
            return False
    return True