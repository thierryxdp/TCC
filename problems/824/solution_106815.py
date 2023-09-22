def uppCons(frase):
    i = 0
    saida = ''
    while i < len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            saida = saida + str.upper(frase[i])
        i = i+1
        elif frase[i] not in 'qwrtypsdfghjklçzxcvbnm':
            saida = saida + frase[i]
        i = i+1
    return saida