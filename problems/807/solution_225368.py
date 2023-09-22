def conta_frase(texto):
    """Função que conta a quantidade de frases em um texto."""
    """string->int"""
    return len(texto.split('.','/','!','?','...'))