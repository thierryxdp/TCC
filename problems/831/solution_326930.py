def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	codigo = ''
    for letra in frase:
        if letra in 'aeiou':
            letra = letra + "p" + letra
    return codigo