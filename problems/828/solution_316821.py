def primo(n):
    if n < 2:
        return False
    for d in range(2,n):
        if n%d == 0:
            return False
    return True