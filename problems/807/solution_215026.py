# A função foi definida de tal modo que ela conta o numero de frases no texto
#Com o Len meu programa conta caracteres
#O replace substitui uma frase especificada por outra frase especificada.
def conta_frases(frase):
    """A função analisa os pontos ortograficos
       str -> int"""
    frase1 = frase.replace("...", "!")
    frase2 = frase1.replace("?", "!")
    frase3 = frase2.replace(".", "!")
    return len(frase3.split('!'))-1