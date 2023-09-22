def uppCons(frase):
    consoantes="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    toUpper = ['a', 'e', 'i', 'o', 'u', 'y']
    array = []
    for c in frase:
        
        if c in toUpper:
            c = c.upper()
            array.append(c)
    return(''.join(array))