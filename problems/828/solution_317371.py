def primo(numero):
    j = 0
    for i in range(1, numero):
        if numero%i ==0:
            j += 1
    if j == 2:
        return True
    else:
        return False