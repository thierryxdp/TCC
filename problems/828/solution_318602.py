def primo(numero):
    contador = 0
    for num in range(1, numero + 1):
        if numero % num == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False