def conta_frases(frases):
    """
    Função que recebe uma string e retorna a quantidade de frases contidas na string
    str --> int
    """
    return frases.count('. ')+frases.count('?')+frases.count('!')+frases[-1:].count('.')