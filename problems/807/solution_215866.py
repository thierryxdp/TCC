def conta_frases(frase):
    """Funcao calcula e retorna a quantidade de frases em um texto;string-->int"""
    return frase.count('. ','!','?','...')