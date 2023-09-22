def uppCons(frase):
    fraseConsoante =''
    i = 0
    while i < len(frase):
        if not frase[i] in 'aeiouAEIOU' and frase[i].isalpha() or frase[i] =='ç':
            fraseConsoante += frase[i].upper()
        else :
            fraseConsoante += i
        i += 1

    return fraseConsoante