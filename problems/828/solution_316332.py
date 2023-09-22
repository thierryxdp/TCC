def primo(n):
    vezes = 0
    listaNum = list(range(1, n + 1))
    for i in range(len(listaNum)):
        if n % listaNum[i] == 0:
            vezes = vezes + 1
    if vezes > 2:
        return False
    else:
        return True