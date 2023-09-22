def conta_frases(frase):
    """calcula e retorna a quantidade de frases de um texto de entrada; str, str -> int"""
    return len(str.split(str.strip(frase,"?")))