def uppCons(frase):
    i = 0
    while i < len(frase):
        frase = frase.split
        if frase[i] not in "AEIOUaeiou":
            frase[i].upper()
        i += 1
    return ''.join(frase)