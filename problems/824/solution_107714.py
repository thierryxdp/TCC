def uppCons(frase):
    retorno = ''
    for caractere in frase:
        if caractere.islower('aeiou'):
            retorno += caractere.upper('aeiou')
    return retorno