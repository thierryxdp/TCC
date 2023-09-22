def lingua_p(palavra):
    palavra.lower
    vogais= "aàáãâeéêiíoóô"
    alterada = ""
    for letra in vogais:
        if letra in vogais:
            alterada = letra + "p" + letra
        else:
            alterada+= letra
    return alterada