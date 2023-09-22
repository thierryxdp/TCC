def conta_frases(frases):
    """retorna o numero de frases"""
    return len(str.join(" "(str.split(frases,'!'))))