def uppCons(frase):
    completar = ''
    proximo = 0
    while proximo<len(frase):
        if frase[proximo] not in 'AEIOUaeiou':
            completar+str.upper(frase[proximo])
        proximo = proximo + 1
    return completar