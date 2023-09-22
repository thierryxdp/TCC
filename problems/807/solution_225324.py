def conta_frases(frases):
    """Função que conta o número de frases que aparecem em um dado texto; str->int"""
    x = str.count(frases,'...')
    y = str.count(frases, '.')
    z = str.count(frases, '?')
    w = str.count(frases, '!')
    return (y + z + w) - 2*x