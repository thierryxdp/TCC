def lingua_p(mot):
    """Recebe como argumento uma palavra e a raduz para 
    a lingua do p
    str->str"""
    word=str.lower(mot)
    palavra=str.split(mot)
    vogais=['a','e','i','o','u']
    retorno=''
    for letra in :
        if letra in word:
            retorno=retorno + letra + 'p' + letra
        else:
            retorno=retorno+letra
    return retorno