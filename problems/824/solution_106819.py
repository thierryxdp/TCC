def uppCons(frase):
    i = 0
    saida = ''
    while i < len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNM ':
            saida = saida + str.upper(frase[i])
        i = i+1
    return saida