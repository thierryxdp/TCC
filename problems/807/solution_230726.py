def conta_frases(texto):
    """contará o número de frases dentro de um texto
    string-->int"""
    if "!"and"."and"?"and"..." in texto:
        return str.split(texto)