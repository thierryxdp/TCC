def primo(n):
    for d in range(2,n):
        if n/d!=n//d:
            return True
        else:
            return False
    return True or False