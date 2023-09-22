def conta_frases(frase):
    """..."""
    s = frase
    ret = 3*"."
    ponto = s.split(ret)
    interrogacao = s.split("?")
    exclamacao = s.split("!")
    return len(exclamacao) + len(ponto) + len(exclamacao)