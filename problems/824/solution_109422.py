def uppCons(frase):
    fraseConsoante =''
    i = 0
    while letra < len(frase):
        if not i in 'aeiouAEIOU' and i.isalpha() or i =='ç':
            fraseConsoante += i.upper()
        else :
            fraseConsoante += i
        i += 1

    return fraseConsoante