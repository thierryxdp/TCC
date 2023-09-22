def primo(n):
    if n<=1:
        return False
    elif n==2:
        return True
    for contador in range(2,n):
        if n%contador == 0:
            return False
    return True