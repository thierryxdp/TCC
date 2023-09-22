def uppCons(frase):
    i = 1
    NF=str.upper(frase)
    while i < len(NF):
        if NF[i] in 'AEIOU':
            NF = str.lower(NF[i])
        i = i + 1
    return NF