def conta_frases(texto):
    import re
    return len(re.split(".|?|!", texto))