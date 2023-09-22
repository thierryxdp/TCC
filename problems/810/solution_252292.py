def inverte (Frase):
    """Inverta a Frase da entrada, deixando todas as letras maisculas e minusculas e removendo todas as pontuações. """
    Frase1 = Frase.replace (',', ' ')
    Frase2 = Frase1.replace ('.', ' ')
    Frase3 = Frase2.replace (';', ' ')
    Frase4 = Frase3.replace ('!', ' ')
    Frase5= (str.lower(Frase4))
    Frase6= ( list(reversed (Frase5)))
    return Frase6