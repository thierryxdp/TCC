def uppCons(frase):
    retorno = ''
    i='aeiou'
    for caractere in frase:
        if caractere.islower(i):
            retorno += caractere.upper(i)
    return retorno