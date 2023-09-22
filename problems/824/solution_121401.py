def uppCons(frase0):
    i = 0
    frase1= ''
    while i<len(frase0):
        if frase0[i] in 'bcdfghjklmnpqrstvwxyzç':
            frase1 = frase1 + str.upper(frase0[i])
        else:
            frase1 = frase1 + frase0[i]
        i=i+1
    return frase1