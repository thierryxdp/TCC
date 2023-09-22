def conta_frases(texto):
    """Retorna a quantidade de frases existentes em um texto
       Entrada: str
       Saida: int
    """
    x = texto.split('.', '!', '?', '...')
    return len(x)