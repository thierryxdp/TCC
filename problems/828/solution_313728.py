def primo(n: int):
    
    for numero in list(range(1, n+1)):
        if numero % 2 == 0 or numero % 3 == 0:
            return True
        else:
            return False