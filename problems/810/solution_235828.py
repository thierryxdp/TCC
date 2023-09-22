def inverte(frase):
    for char in ".!?,-":
        frase = frase.replace(char, "")
    z = str.split(frase, ' ')
    x = str.join(' ', z)
    return x.reverse()