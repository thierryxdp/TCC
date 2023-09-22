def uppCons(frase):
    completar = ''
    proximo = 0
    while proximo<len(frase):
        if frase[proximo] in 'AEIOUaeiou':
            completar+frase[proximo]
        proximo = proximo + 1
    return completar