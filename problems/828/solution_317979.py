def primo(numero):
    c = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            c += 1
    return c == 2