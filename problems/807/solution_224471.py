def conta_frases(frase):
    """A função analisa os pontos ortograficos e conta o número de
    frases que aparece str -> int"""
    frase1 = frase.replace("...", "!")
    frase2 = frase1.replace("?", "!")
    frase3 = frase2.replace(".", "!")
    return len(frase3.split('!'))-1