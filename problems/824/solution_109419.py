def uppCons(frase):
    fraseConsoante =''
    i = 0
    while i < len(frase):
        if not letra in 'aeiouAEIOU' and letra.isalpha():
            fraseConsoante += letra.upper()
        else :
            fraseConsoante += letra
        i += 1

    return fraseConsoante