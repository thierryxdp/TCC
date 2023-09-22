def primo(n):
    if n%2 == 0:
        return False
    for numero in range(3,n,2):
        if n%numero == 0:
            return False
    return True