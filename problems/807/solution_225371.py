def conta_frases(texto):
    """Função que conta a quantidade de frases em um texto."""
    """string->int"""
    ponto=['.','!','...','?']
    return texto.count(ponto)