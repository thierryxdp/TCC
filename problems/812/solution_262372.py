def conta_frases(frase):
    """A função analisa os pontos ortograficos e os remove da frase
       str -> str"""
    frase1 = frase.replace("...", "!")
    frase2 = frase1.replace("?", "!")
    frase3 = frase2.replace(".", "!")
    return len(frase3.split('!'))-1