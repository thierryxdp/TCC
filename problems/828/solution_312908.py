def primo(n):
    for c in range(1, n):
        if n % c == 0:
            return False 
        else:
            return True