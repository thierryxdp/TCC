def q(frase):
    """Uma função que dado dois números, retorna uma piramide de numeros"""
    """int, int -> list"""
    frase = frase.replace('!', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('...', ' ')
    frase = frase.split('  ')
    return len(frase) - 1