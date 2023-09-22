def primo(n):
    if n%2==0:
        return True
    for i in range(3,n,2):
        if n%i==0:
            return False
    return True