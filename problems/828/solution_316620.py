def primo(n):
    if n%2==0:
        return True
    for i in range(2,n,):
        if n%i==0:
            return False
    return True