def conta_frases(texto):
    """conta quantas freases tem no texto"""
    a = str.split(texto,"...")
    a = str.split(a,"!")
    a = str.split(a, "?")
    a = str.split(a, ".")
    
    return len(a)