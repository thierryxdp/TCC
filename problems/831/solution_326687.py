def lingua_p(palavra):
    palavra.lower
    vogais= "aàáãâeéêiíoóôúu"
    alterada = ""
    for letra in palavra:
        if letra in vogais:
            alterada += letra + "p" + letra
        else:
            alterada += letra
    return alterada