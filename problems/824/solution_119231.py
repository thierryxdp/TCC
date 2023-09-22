def uppCons(frase):
    novafrase = ''
    for i in frase:
        if i not in 'aeiou':
            novafrase.append(i.upper())
        else:
            novafrase.append(i)
    return novafrase