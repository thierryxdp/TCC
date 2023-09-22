def uppCons(frase):
    vogal=['a','e','i', 'o','u']
    for i in range(len(frase)):
        if frase[i] not in vogal:
            map(frase.upper(),frase[i])
    return frase