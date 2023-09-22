def uppCons(frase):
    i=0
    saida=''
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOUÁÉÍÓÚÃÕÊÎÔÂÛ':
            saida = saida + str.upper(frase[i])
        i = i+1
    return saida