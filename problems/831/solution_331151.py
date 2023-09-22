def lingua_p(palavra):
    stringaux = ""
    vogais = "aeiou"
    for i in palavra:
        stringaux += i
        if i in vogais:
            stringaux = stringaux + "p" + i
    return stringaux