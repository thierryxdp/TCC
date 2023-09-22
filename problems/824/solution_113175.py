def uppCons(frase):
    '''str --> str'''
    i = 0
    retorno=''
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU':
            retorno = retorno+frase[i].upper()
        else:
            retorno = retorno+frase[i]
        i = i+1
    return retorno