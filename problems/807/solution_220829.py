def conta_frases(frases):
    """..."""
    x = frases.count('.' or '!'  or '?' or '...')
    return len(x)