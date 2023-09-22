def uppCons (fraseDada):
    s = ""
    for letra in fraseDada:
        if letra in "bcçdfghjklmnpqrstvxwyz":
            s += letra.upper() 
        else: 
            s+=letra
    return s