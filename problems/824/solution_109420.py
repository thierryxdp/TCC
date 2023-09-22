def uppCons(frase):
    fraseConsoante =''
    letra = 0
    while letra < len(frase):
        if not letra in 'aeiouAEIOU' and letra.isalpha():
            fraseConsoante += letra.upper()
        else :
            fraseConsoante += letra
        letra += 1

    return fraseConsoante