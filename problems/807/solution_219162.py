def conta_frases(frase: str) -> int:
    """dhjgdfjg"""
    frase = frase.replace("...", "A")
    frase = frase.replace("?", "A")
    frase = frase.replace(".", "A")
    frase = frase.replace("!", "A")
    conta_frases = frase.count('A')
    return conta_frases