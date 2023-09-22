def primo(num):
    """Recebe um numero e verdaderio ou falso caso este ja um prima;
    int --> bool"""

    if (num % 2 == 0):
        # Caso o num seja par 
        return False
    
    
    for iii in range(3, num, 2):
        if (num % iii == 0):
            return False

    return True