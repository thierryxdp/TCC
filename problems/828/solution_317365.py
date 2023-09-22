def primo(numero):
    i = 1
    j = 0
    while i < numero:
        if numero%i == 0:
            j += 1
            i += 1
        else:

            if j == 2:
                return True
            else:
                return False