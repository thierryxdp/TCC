def primo(n):
    divisores = 0
    for x in range(2, n):
        if n%x == 0:
            divisores = divisores + 1
    if divisores == 0:
        return True
    else:
        return False