def primo(numero):
    """recebe um numero e retorna true se ele for primo
    int -> bool"""
    
    d = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            d += 1
            
    if d == 2:
        return True
    
    elif numero == 1:
        return True
    
    else:
        return False