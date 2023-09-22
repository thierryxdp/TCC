def primo(n):
    if n % 2 == 0:
        return False
    for a in range(3,n,2):
        if n % a == 0:
            return False
    return True