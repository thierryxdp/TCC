def primo(Num):
    divisores = 0
    for c in range(1, Num + 1):
        if Num % c == 0:
            divisores = divisores + 1
    if divisores == 2:
        return True
    else:
        return False