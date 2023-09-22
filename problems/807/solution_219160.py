def conta_frases(frase: str) -> int:
    """dhjgdfjg"""
    frase = frase.replace("...", "A")
    frase = frase.replace("?", "A")
    frase = frase.replace(".", "A")
    frase = frase.replace("!", "A")
    return frase.count('A')