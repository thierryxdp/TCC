def inverte (Frase1):
    """Inverta a Frase da entrada, deixando todas as letras maisculas e minusculas e removendo todas as pontuações. """
    Frase2= (str.lower(Frase1))
    Frase3= list(reversed (Frase2))
    return Frase3