def conta_frases(texto):
    """funcao que retorna a quantidade de frases em um texto; str-> int"""
    return texto.count('!')+texto.count('...')+texto.count('?')+(texto.count('.')-(3*texto.count('...')))