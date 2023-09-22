def lingua_p(palavra):
    palavra.lower
    vogais= "aàáãâeéêiíoóôú"
    alterada = ""
    for letra in vogais:
        if letra in vogais:
            alterada = letra + "p" + letra
        else:
            alterada+= letra
    return alterada