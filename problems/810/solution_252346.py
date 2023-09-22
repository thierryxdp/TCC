def inverte (Frase):
    """Inverta a Frase da entrada, deixando todas as letras maisculas e minusculas e removendo todas as pontuações. """
    Frase1 = Frase.replace (',', ' ')
    Frase2 = Frase1.replace ('.', ' ')
    Frase3 = Frase2.replace (';', ' ')
    Frase4 = Frase3.replace ('!', ' ')
    Frase5 = Frase4.replace ('?', ' ')
    Frase6 = Frase5.replace (':', ' ')
    Frase6 = str.split (Frase5, ' ' )
    Frase7 = list.reverse(Frase6)
    Frase8 = str.join (' ',Frase7)
    return Frase8