def conta_frases(frases):
    """retorna o numero de frases de um texto, str->int"""
    frases1=frases.split("...")
    frase1=frases.split(".")
    frases1=frases.split("!")
    frases1=frases.split("?")
    frases1=frases.strip( )
    return len(frases1)