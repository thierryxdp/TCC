def primo(n):
    div = 0
    i=0
    while i<=n:
        if n%i == 0:
            div += 1
            i+= 1
        else:
            i += 1
    if div > 2:
        return False
    else:
        return True