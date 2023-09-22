def uppCons(frase):
    for i in frase:
        if i not in 'AEIOUaeiou':
            i.upper()
    return frase