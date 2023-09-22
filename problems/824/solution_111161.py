def uppCons(frase):
    i = 0
    frase_alterada = list()
    while i < len(frase):
        if (str.lower(frase[i]) not in ('aeiou')):
            list.append(frase_alterada, str.upper(frase[i]))
        else:
            list.append(frase_alterada, frase[i])
            i += 1
    return str.join('', frase_alterada)