def lingua_p(palavra):
    """str -> str"""
    palavra_nova = ""
    for letra in palavra.lower():
        if letra in "áéíóúaeiou":
            palavra_nova += letra + "p" + letra
        else:

            palavra_nova += letra

    return palavra_nova