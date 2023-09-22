def lingua_p(palavra):
    palavra.lower
    vogais= "aàáãâeéêiíoóôú"
    alterada = ""
    for letra in palavra:
        if letra in vogais:
            alterada += letra + "p" + letra
        else:
            alterada += letra
    return alterada