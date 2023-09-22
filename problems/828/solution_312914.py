def primo(n):
    for c in range(2, n):
        if n % c == 0:
            return False 
        else:
            return True