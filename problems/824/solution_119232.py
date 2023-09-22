def uppCons(frase):
    novafrase = ''
    for i in frase:
        if i not in 'aeiou':
            novafrase += i.upper()
        else:
            novafrase += i
    return novafrase