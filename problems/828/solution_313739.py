def primo(n: int):
    
    for numero in list(range(2, n+1)):
        if numero % 2 == 0 and numero % 3 == 0:
            return True
        else:
            return False