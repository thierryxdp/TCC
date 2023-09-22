def uppCons(frase):
    proximo = 0
    if frase[proximo] not in 'AEIOUaeiou':
        return str.upper(frase)
    else:
        return frase