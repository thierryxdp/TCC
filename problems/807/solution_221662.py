def conta_frases(frases):
    """
    str-> int"""
    frases_modificadas=frases
    frases_modificadas=frases_modificadas.replace("...",".")
    frases_modificadas=frases_modificadas.replace("!",".")
    frases_modificadas=frases_modificadas.replace("?",".")
    return len(frases_modificadas.split("."))+1