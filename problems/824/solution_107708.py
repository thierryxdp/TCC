def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] in 'qertypsdfghjklçzxcvbnm':
            frase = str.upper[i]
        i = i + 1
    return frase