def primo(numero):
    """Indica se o número dado é ou não primo.
       int -> bool"""
    
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    for i in range(2,numero):
        if numero % i == 0:
            return False
        
    return True