def primo(n):
    for numero in range(1, n):
        if numero % n == 0:
            return True
        
        if not numero % n == 0:
            return False