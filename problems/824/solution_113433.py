def uppCons (frase):
    ''''''
    frasefinal = ''
    i = 0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiouÁÉÍÓÚáéíóúÂÊâêÀàÃã':
            frasefinal += str.upper(frase[i])
        else:
            frasefinal+= frase[i]
        i += 1
    return frasefinal