def uppCons(frase):
    consoantes_min = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    i = 0
    while i < len(frase):
        if frase[i] in consoantes_min:
            letra = str(frase[i])
            frase[:i] + letra.upper() + frase[i+1:]
        i += 1
    return frase