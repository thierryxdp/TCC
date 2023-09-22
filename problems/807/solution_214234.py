def conta_frases(texto):
    """Testando ainda"""
    separadorponto = str.split(texto,".")
    separadorinterr = str.split(texto,"?")
    separadorexc = str.split(texto,"!")
    separadorret = str.split(texto,"...")
    return int(len(separadorponto)) + int(len(separadorinterr)) + int(len(separadorexc)) + int(len(separadorret))