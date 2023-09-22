def uppCons(frase):
    retorno = ''
    for caractere in frase:
        if caractere.isupper():
            retorno += caractere.lower()
    return frase