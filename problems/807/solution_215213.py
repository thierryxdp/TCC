def conta_frases(texto):
    
    
    if texto.count("...") == 0:
        n1 = 0
    else:
        n1 = texto.count("...")
        l1 = texto.split("...")
        texto = str.join("", l1)
    
    n2 = texto.count(".")
    n3 = texto.count("?")
    n4 = texto.count("!")
    
    return n1+ n2 + n3 + n4