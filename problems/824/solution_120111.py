def uppCons(frase):
    i = 0
    frase_maiuscula = ' ' 
    while i < len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            frase_maiuscula += frase[i].upper()
        else:
            frase_maiuscula += frase[i]
        i += 1
    return frase_maiuscula