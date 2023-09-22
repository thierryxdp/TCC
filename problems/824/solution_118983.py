def uppCons(frase):
    FRaSe = ''   
    c = 0
    while c < len(frase):
        if str.lower(frase[c]) not in 'aeiou':
            FRaSe = FRaSe + str.upper(frase[c])
        else:
            FRaSe = FRaSe + frase[c]
        c += 1
    return FRaSe