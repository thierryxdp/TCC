def lingua_p(palavra):
    fraseNew = ""
    x = 0
    vogais = "a","e","i","o","u"
    for i in palavra:
        if i in vogais:
            fraseNew = fraseNew + "p"
        fraseNew = fraseNew + str(vogais)
    return fraseNew