def primo(numero):
    qtd_divisores = 0
    for x in range(1,numero+1):
        if numero%x == 0:
            qtd_divisores = qtd_divisores + 1
    if qtd_divisores == 2:
        return True
    else:
        return False