def conta_frases(texto):
    """essa funçao recebe um texto e retorna a quantidade de frases presentes neles, a partir do numero de pontos finais, de exclamaçao, de interrogaçao e reticencias"""
    """entrada: str"""
    """saida: int"""
    return str.count(texto, '.')+str.count(texto, '!')+str.count(texto, '?')+(str.count(texto,'...')-2)