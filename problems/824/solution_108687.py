def uppCons(frase):
    """ """
    indice = 0
    while indice < len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            maiuscula = frase[indice].upper()
            frase = frase.replace(frase[indice],maiuscula,1)
        indice += 1
    return frase