def conta_frases (texto):
    """Conta quantas frases estão presentes em um texto 
    dado pelo usuário.
    str -> int"""
    return str.count(texto, ".")+str.count(texto, "!")+str.count(texto, "?") -2*str.count(texto, "...")