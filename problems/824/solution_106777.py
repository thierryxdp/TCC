def uppCons(frase):
    saida = ''
    proximo = 0
    while proximo < len(frase):
        if 'qwrtypsdfghjklçzxcvbnm' in frase[proximo]:
            saida = saida + str.upper(frase[proximo])
        proximo = proximo+1
    return saida