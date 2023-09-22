def uppCons(frase):
    consoantes="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    toUpper = ['a', 'e', 'i', 'o', 'u', 'y']
    array = list(frase)
    for i,c in enumerate(array):
        if c in toUpper:
            array[i] = c.upper()
    return ("".join(array))