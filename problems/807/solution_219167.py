def conta_frases(frase: str) -> int:
    """dhjgdfjg"""
    frase = frase.replace("...", "#")
    frase = frase.replace("?", "#")
    frase = frase.replace(".", "#")
    frase = frase.replace("!", "#")
    conta_frases = frase.count('#')
    return conta_frases