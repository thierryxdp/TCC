def carros(pessoas,capacidade=5):
    """retorna o numero necessario de carros."""
    import match
    return match.ceil(pessoas/capacidade)