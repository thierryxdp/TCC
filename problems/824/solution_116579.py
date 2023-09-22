def uppCons(frase):
    s = ''
    for i in frase:
        if i not in 'aeiou':
            s += i.upper()
        else:
            s += i
    return s