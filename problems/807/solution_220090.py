def conta_frases(frases):
    """retorna o numero de frases de um texto, str->int"""
    frases1=frases.replace("...",".")
    frases1=frases.replace(".","?")
    frases1=frases.replace("?","!")
    frases1=frases.replace("!","/")
    frases1=frases.replace("/"," ")
    return (frases1.split(" "))