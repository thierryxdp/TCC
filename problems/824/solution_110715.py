def uppCons (fraseDada):
    s = ""
    for letra in fraseDada:
        if letra in "bcdfghjklmnpqrstvxwyz":
            s += letra.upper() 
        else: 
            s+=letra
    return s