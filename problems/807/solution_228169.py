def conta_frases(texto):
    """determina a quantidade de frases em um texto, sejam elas
    terminadas em ponto, ponto de interrogação, reticências ou em
    ponto de exclamaçao"""
    
    return len((texto).split("."))