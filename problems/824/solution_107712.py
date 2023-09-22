def uppCons(frase):
    retorno = ''
    caractere = 'aeiou'
    for caractere in frase:
        if caractere.islower():
            retorno += caractere.upper()
    return retorno