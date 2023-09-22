def uppCons(frase):
    i=o
    saida=''
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU':
            saida = saida + frase[i]
        i = i+1
    return saida