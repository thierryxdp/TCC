def conta_frases(texto):
    """Função que retorna quantas frases tem em um texto"""
    return len(texto.count('.')) or len(texto.conunt('!')) or len(texto.count('?')) or len(texto.count('...'))