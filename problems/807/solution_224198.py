def conta_frases(frase):
    a=int(frase.count("."))
    b=int(frase.count("?"))
    c=int(frase.count("!"))
    d=int(frase.count("..."))
    if "..." in frase:
        return a+b+c+d - 3
    if d==2:
        return 4
    else:
        return a+b+c+d