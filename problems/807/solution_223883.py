def conta_frases(texto):
    """retorna por quantas frases o texto é formado"""
    """str -> int"""
    return len(texto.split('.')) + len(texto.split('!')) + len(texto.split('?')) +len(texto.split('...'))-1  -3*(len(texto.split('...')))