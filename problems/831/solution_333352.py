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
        cont = cont + p
    return cont