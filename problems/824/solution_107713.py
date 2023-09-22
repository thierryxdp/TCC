def uppCons(frase):
    retorno = ''
    for 'aeiou' in frase:
        if 'aeiou'.islower():
            retorno += 'aeiou'.upper()
    return retorno