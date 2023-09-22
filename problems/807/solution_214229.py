def conta_frases(texto):
    """Testando ainda"""
    separadorponto = str.split(texto)
    return int(len(separadorponto)) + int(len(str.split(texto,"?")) + int(len(str.split(texto,"!")) + int(len(str.split(texto,"..."))