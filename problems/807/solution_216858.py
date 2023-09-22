def conta_frases(texto):
    """Função que retorna a quantidade de frases de um texto;str->int"""
    texto=str.split(texto)
    return len(texto,'.')