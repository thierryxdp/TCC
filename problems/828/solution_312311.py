def primo(n):
    for numero in [2, n+1]:
        if n%numero == 0:
            return False
        else:
            return True