def conta_frases(s: str) -> int:
    """ dado um texto armazenado em uma string, retorna o número de frases
    que aparecem neste texto."""
    s == ()
    a = str.replace(s, "...", ".")
    
    return s.count("?") + s.count("!") + a.count(".")