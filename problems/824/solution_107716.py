def uppCons(frase):
    retorno = ''
    for caractere in 'aeiou':
        if caractere.islower():
            retorno += caractere.upper()
    return retorno