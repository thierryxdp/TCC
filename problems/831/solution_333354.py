def lingua_p(f):
    cont = ""
    for p in f:
        if p == "a":
            p += "pa"
        elif p == "e":
            p += "pe"
        elif p == "i":
            p += "pi"
        elif p == "o":
            p += "po"
        elif p == "u":
            p += "pu"
        elif p == "á":
            p += "pá"
        elif p == "é":
            p += "pé"
        elif p == "ú":
            p += "pú"
        cont = cont + p
    return cont