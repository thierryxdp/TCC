def uppCons(frase):
    retorno = ''
    for caractere in frase:
        if caractere.islower():
            retorno += caractere.upper()
    return retorno