def primo(n: int):
    
    for numero in list(range(2, n+1)):
        if n % numero == 0:
            return False
        else:
            return True