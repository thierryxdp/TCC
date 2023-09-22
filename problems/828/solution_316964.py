def primo(n):
    if n < 2:
        return False
    for d in range(2,n):
        if d%n==0:
            return False
        else:
            return True