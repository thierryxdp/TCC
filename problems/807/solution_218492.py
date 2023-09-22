def conta_frases(frase):
    """..."""
    s = frase
    ponto = s.split(".")
    interrogacao = s.split("?")
    exclamacao = s.split("!")
    return len(exclamacao)