def conta_frases(texto):
    """contará o número de frases dentro de um texto
    string-->int"""
    if "!"or"."or"?"or":" in texto:
        return str.strip(texto,"!"or"."or"?"or":")