def lingua_p(mot):
    """Recebe como argumento uma palavra e a raduz para 
    a lingua do p
    str->str"""
    str.lower(mot)
    palavra=str.split(mot)
    vogais='aeiou'
    retorno=''
    for letra in palavra:
        if letra in vogais:
            retorno=retorno + letra + 'p' + letra
        else:
            retorno=retorno = letra
    return retorno