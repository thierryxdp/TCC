def primo(n):
    """"""
    for num in range(2, n-1):
        if num % n == 0:
            return False
        
    return True