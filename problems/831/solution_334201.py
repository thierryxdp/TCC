def lingua_p(palavra):
    """Determinar a palavra com p antes e depois de cada vogal;
    str -> str"""
    palavra_nova = ""
    for letra in palavra.lower():
        if letra in "áéíóúaeiou":
            palavra_nova += letra + "p" + letra
        else:
            palavra_nova += letra
    return palavra_nova