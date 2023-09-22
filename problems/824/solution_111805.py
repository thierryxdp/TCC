def uppCons(frase):
    novafrase = ''
    tamanho = len(frase)
    i = 0
    while i < tamanho:
        if not frase[i] in 'aeiouAEIOU':
            novafrase = novafrase + str.upper(frase[i])
        i += 1
    return novafrase