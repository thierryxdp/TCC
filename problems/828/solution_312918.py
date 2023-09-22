def primo(n):
    for c in range(2, n - 1):
        if n % c == 0:
            return False 
        else:
            return True