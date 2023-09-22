def primo(n):
    qtd = 0
    for div in range(1,n+1):
        if (n % div == 0):
            qtd += 1
    if (qtd == 2):
        return True
    else:
        return False