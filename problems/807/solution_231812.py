def conta_frases(texto):
    """Retorna o número de frases em um texto
    assinatura: str -> int"""
    Lista = str.split(texto,x)
    separador = ['.', '!', '?', '...']
    for x in separador:
        return Lista