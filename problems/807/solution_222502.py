def conta_frases(texto):
    """Função que retorna quantas frases tem em um texto"""
    return len(texto.split('.')) and len(texto.split('!')) and len(texto.split('?')) and len (texto.split('...'))