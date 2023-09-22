def inverte (Frase):
    """Inverta a Frase da entrada, deixando todas as letras maisculas e minusculas e removendo todas as pontuações. """
    Frase1 = Frase.replace (',', ' ')
    Frase2 = Frase1.replace ('.', '')
    Frase3 = Frase2.replace (';', ' ')
    Frase4 = Frase3.replace ('!', '')
    Frase5 = Frase4.replace ('?', '')
    Frase6 = Frase5.replace (':', ' ')
    Frase7 = Frase6.replace ('-', ' ')
    Frase8 = str.lower (Frase7)
    Frase9 = str.split (Frase8, ' ' )
    Frase10 = list.reverse(Frase9)
    Frase11 = str.join (' ',Frase9)
    return Frase11