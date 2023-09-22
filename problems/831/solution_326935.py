def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	codigo = ''
    for letra in palavra:
        if letra in 'aeiou':
            codigo += letra + "p" + letra
        else:
            codigo += letra
    return codigo