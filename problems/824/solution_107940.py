def uppCons(frase):
    i = 0
    vogais = 'aeiouAEIOUãõáóíéúÃÕÁÉÍÓÚ'
    while i < len(frase):
        if frase[i] not in vogais:
            frase = frase.replace(frase[i], str.upper(frase[i]))
        i += 1
    return frase