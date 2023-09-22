def conta_frases(texto):
    """Função que retorna a quantidade de frases presentes no texto dado"""
    return len(split(split(split(split(texto,'.'),'?'),'...'),'!'))