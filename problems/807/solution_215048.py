def conta_frases (texto):
    """Conta quantas frases estão presentes em um texto 
    dado pelo usuário.
    str -> int"""
    x=texto
    if x.count ("!") > 0:
        x = str.replace (x, "!", ".")
    if x.count ("?") > 0:
        x = str.replace (x, "?", ".")
    if x.count ("...") > 0:
        x = str.replace (x, "...", ".")
        return len (str.split (x, ".")