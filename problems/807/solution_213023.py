def conta_frases(texto):
    """Função que conta o número de frases presentes em um texto; string -> int"""
    texto = str.replace(texto, '...', '!')
    return str.count(texto, '.') + str.count(texto, '!') + str.count(x, '?')