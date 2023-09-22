def primo(n):
    if n==2:
        return True
    for d in range(2,n):
        if n%d==0:
            return False
        else:
            return True