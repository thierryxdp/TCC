def primo(n):
    if n == 1:
        return False
    if n == 2:
        return True
    qtd = 0
    for i in range(n):
        if (n%(i+2)) == 0:
            qtd = qtd + 1
    if qtd == 0:
        return True
    else:
        return False