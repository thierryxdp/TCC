def conta_frases(texto):
    """retorna o numero de frases dado o texto de entrada levando em conta a pontuação"""
    frase = texto.split()
    return texto.count(texto,frase)