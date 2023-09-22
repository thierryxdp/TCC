def uppCons(frase):
    consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    i = 0
    while i < len(frase):
        if frase[1] in consoantes:
            frase.upper(frase[i])
        i += 1
    return frase