def lingua_p(palavra):
    a = ""
    for letra in palavra:
        if letra.lower() in "aáéeiou":
            a = a + letra + "p" + letra
        else:
            a = a + letra
    return a.lower()