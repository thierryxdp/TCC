def conta_frases(frase):
    """..."""
    s = frase
    ponto = s.split(".")
    interrogacao = s.split("?")
    exclamacao = s.split("!")
    reticencias = s.split(ret)
    return len(ponto + interrogacao + exclamacao)