def conta_frases(text):
    """Recebe um texto e retorna a quantide de frases separadas por pontos, reticencias
    pontos de exlcamacao e pontos de exlcamacao;
    str --> int"""

    buffer_count = 0

    # Conta as frases separadas por '?', '!' e '.'
    buffer_count += str.count(text, '?')
    buffer_count += str.count(text, '!')
    buffer_count += str.count(text, '.')
    
    # Subtrai os '.' contados anteriomente caso tenha reticencias
    buffer_count -= (2 * str.count(text, '...'))

    return buffer_count