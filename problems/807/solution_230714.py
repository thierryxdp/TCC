def conta_frases(texto):
    """contará o número de frases dentro de um texto
    string-->int"""
    x=str.split(texto)
    if "!"or"."or"?"or":" in texto:
        return x
    return len(x)