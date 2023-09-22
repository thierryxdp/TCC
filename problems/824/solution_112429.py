def uppCons(frase):
    i=0
    novaF=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            novaF=novaF + str.upper(frase[i])
        else:
            novaF=novaF+frase[i]
        i=i+1
    return novaF