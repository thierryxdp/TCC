def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] in 'qwrtypsdfghjklzxcvbnmç':
            letra = str.upper(frase[i])
            frase = frase[:i] + letra + frase[i + 1:]
        i = i + 1
    return frase