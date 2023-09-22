def uppCons(frase):
    i=0
    saida=''
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU':
            saida = saida + str.upper(frase[i])
        i = i+1
    while i<len(frase):
        if frase[i] in 'aeiouAEIOU':
            saida = saida + frase[i]
        i = i+1
    return saida