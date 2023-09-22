def uppCons(frase):
    i = 0
    j = ''
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ':            
            j = j + str.upper(frase[i])
        else:
            j = j + frase[i]
        i = i + 1
    return j