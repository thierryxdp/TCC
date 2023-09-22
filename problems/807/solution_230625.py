def conta_frases(texto):
    s= (str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "...") + str.count(texto, "?")
        if "..." in x: 
        s= s + (str.count(texto, "...")) * (-3)
        return s
    else:
        return (str.count(texto, ".") + str.count(texto, "?") + str.count(texto, "...") + str.count(texto, "!")