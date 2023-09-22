def primo(n):
    """ """
    
    for y in range(1, n+1):
        if y > 1 :
            if n%y == 0 and y != n:
                return False
    return True