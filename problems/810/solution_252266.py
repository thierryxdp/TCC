def inverte (Frase):
    """Inverta a Frase da entrada, deixando todas as letras maisculas e minusculas e removendo todas as pontuações. """
    Frase1=  list(reversed (Frase))
    Frase2= str.lower(Frase1)
    Frase3 = Frase2.replace (',', '')
    Frase3 = Frase2.replace ('.', '')
    Frase3 = Frase2.replace (':', '')
    Frase3 = Frase2.replace ('-', '')
    return Frase3