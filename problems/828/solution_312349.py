def primo(n):
    div = 2
    for i in range(2,n):
        if n%i == 0:
            div+=1
    return div

    if divisores(n) == 2:
        return True
    else:
        return False