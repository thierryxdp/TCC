def uppCons(frase):
    saida = ''
    i = 0
    while i<len(frase):
        if 'aeiouAEIOU' in frase[i]:
            saida = frase[i]
        i = i+1
        else:
            saida = str.upper(frase[i])
        i = i+1
    return saida