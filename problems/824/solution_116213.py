def uppCons(frase):
    i=0
    frase_saida=''
    while i<len(frase):
        if frase[i] not in 'aeiou':
            frase_saida=frase_saida+str.upper(frase[i])
            i=i+1
        else:
            frase_saida=frase_saida+frase[i]
            i=i+1
    return frase_saida