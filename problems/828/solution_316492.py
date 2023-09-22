def primo(x):
    """
    dado um número, verifica se o mesmo é primo
    """
    
    for i in range(x-1):
        if x%(i+1)==0 and i>=2:
            return False
        else:
            return True