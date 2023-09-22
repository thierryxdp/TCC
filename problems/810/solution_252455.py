def inverte (Frase):
    """Inverta a Frase da entrada, deixando todas as letras maisculas e minusculas e removendo todas as pontuações. """
    Frase1 = Frase.replace (',', ' ')
    Frase2 = Frase1.replace ('.', ' ')
    Frase3 = Frase2.replace (';', ' ')
    Frase4 = Frase3.replace ('!', ' ')
    Frase5 = Frase4.replace ('?', ' ')
    Frase6 = Frase5.replace (':', ' ')
    Frase7 = str.split (Frase5, ' ' )
    Frase8 = list.reverse(Frase7)
    Frase9 = str.join (' ',Frase6)
    return Frase8