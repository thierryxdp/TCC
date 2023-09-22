def conta_frases(texto):
    """Função que retorna quantas frases tem em um texto"""
    """str--->int"""
    return len(texto.split('.')) + len(texto.split('!')) + len(texto.split('?')) +len(texto.split('...'))-1  -3*(len(texto.split('...')))