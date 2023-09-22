def conta_frases (texto):
    """Função que, dado um texto, conta o número de frases separadas por '.', '...', '?' ou '!'
    entrada: str
    saída: int"""
    x = str.replace(texto, '? ', '. ')
    y = str.replace(x, '! ', '. ')
    z = str.replace(y, '... ', '. ')
    return len(str.split(z, '. '))