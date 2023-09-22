def uppCons(frase):
    novafrase = ''
    tamanho = len(frase)
    i = 0
    while i < tamanho:
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            novafrase = novafrase + str.upper(frase[i])
        else:
            novafrase = novafrase + frase[i]
        i += 1
    return novafrase