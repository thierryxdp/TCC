def primo(numero):
    divisores = 0
    i = 1
    while i <= numero:
        if numero % i == 0:
            divisores = divisores + 1
        i = i + 1
    if divisores == 2:
        return True
    else:
        return False