def inverte(frase):
    for char in ".!?,-":
        frase = frase.replace(char, " ")
    z = str.split(frase, '')
    y = z[::-1]
    x = str.join(' ', y)
    return x