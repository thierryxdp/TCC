def uppCons(frase):
    i = 0
    palavra_mai = ''
    while i < len(frase):
        if frase[i] in 'QWRTYPSDFGHJKLZXCVBNM':
            palavra_mai += frase[i]
        i += 1
    return palavra_mai