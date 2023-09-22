def conta_frases(texto):
    """retorna por quantas frases o texto é formado"""
    """str -> int"""
    return len(str.split(texto,'.','!','?','...'))