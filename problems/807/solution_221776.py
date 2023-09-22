def conta_frases(texto):
    """essa funçao recebe um texto e retorna a quantidade de frases presentes neles, a partir do numero de pontos finais, de exclamaçao, de interrogaçao e reticencias"""
    """entrada: str"""
    """saida: int"""
    if "..." in texto:
        return str.count(texto, '.')+str.count(texto, '!')+str.count(texto, '?')+str.count(texto,'...')-3
    else:
        return str.count(texto, '.')+str.count(texto, '!')+str.count(texto, '?')