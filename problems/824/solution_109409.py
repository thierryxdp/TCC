def uppCons(frase):
    fraseConsoante =''

    for letra in frase:
        if not letra in 'aeiouAEIOU' and letra.isalpha() or letra=='ç':
            fraseConsoante += letra.upper()


        else :
            fraseConsoante += letra

    return fraseConsoante