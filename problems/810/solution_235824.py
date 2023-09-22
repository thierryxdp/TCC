def inverte(frase):
    for char in ".!?,-":
        frase = frase.replace(char, "")
    x = str.split(frase, ' ')
    return x[ : :-1]