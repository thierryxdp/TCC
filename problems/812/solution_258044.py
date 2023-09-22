def a(text):
    chars = "-?!.,"
    for c in chars:
        frase = frase.replace(c, "\\" + c)