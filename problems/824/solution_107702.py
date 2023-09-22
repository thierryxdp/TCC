def uppCons(frase):
    i = 1
    NF=str.upper(frase)
    if NF[i] in 'AEIOU':
        NF2 = str.lower(NF[i])
    return NF2