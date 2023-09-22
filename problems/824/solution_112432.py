def uppCons(frase):
    i=0
    novaF=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiouãõóáúéí':
            novaF=novaF + str.upper(frase[i])
        else:
            novaF=novaF+frase[i]
        i=i+1
    return novaF