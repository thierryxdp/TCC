def uppCons(frase):
    ''''''
    i = 0
    f = frase
    while f[1] < len(frase):
        frase[i] not in 'AEIOUaeiou'
        f = frase(str.upper(f[i]))
        i = i + 1
    return f