def uppCons(frase):
    retorno = ''
    for caractere in frase:
        if caractere.upper():
            retorno += caractere.lower()
            return frase