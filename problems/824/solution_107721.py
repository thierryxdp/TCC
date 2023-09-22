def uppCons(frase):
    retorno = ''
    for caractere in frase:
        if caractere.isupper():
            retorno += caractere.lower()
        else:
            retorno += caractere.upper()
    return retorno