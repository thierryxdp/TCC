def lingua_p(palavra):
    vogais = "aeiouáéíóú"
    lp = ""
    for pos in vogais:
        if palavra[pos] in vogais:
            lp = lp + palavra[pos] + "p" + palavra[pos]
        else:
            lp = lp + palavra[pos]
    return lp