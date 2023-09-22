def uppCons(frase):
    retorno = ''
    i=len(frase)
    for i in 'aeiou':
        if i.islower():
            retorno += i.upper()
    return retorno