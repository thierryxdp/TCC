def uppCons(frase):
    fraseConsoante =''
    i = 0
    while i < len(frase):
        if not frase[i] in 'aeiouAEIOU' and i.isalpha() or i =='ç':
            fraseConsoante += i.upper()
        else :
            fraseConsoante += i
        i += 1

    return fraseConsoante