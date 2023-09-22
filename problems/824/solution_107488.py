def uppCons(frase):
    """calculo e retorno de uma frase que retorne todas as consoantes com letra maiuscula."""
    f = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            f += caractere.upper()
        else:
            f += caractere
    return f