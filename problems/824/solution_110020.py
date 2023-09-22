def uppCons(frase):
    ''''''
    i = 0
    f = frase
    while i < len(frase):
        frase[i] not in 'AEIOUaeiou'
        f = frase(str.upper(f[i]))
        i = i + 1
    return f