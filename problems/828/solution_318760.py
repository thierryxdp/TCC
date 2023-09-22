def primo(nmr):
    contador = 0
    for elemento in range(2, nmr):
        if nmr % elemento == 0:
            contador += 1
    if contador > 0:
        return False
    else:
        return True