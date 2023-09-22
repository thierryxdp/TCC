def primo(n):
    """"""
    for num in range(2, n):
        if num % n == 0:
            return False
        
    return True