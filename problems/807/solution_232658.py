def conta_frases(texto):
    """Função que faz alguma coisa. str->int"""
    interrogacao=texto.count("?")
    exclamacao=texto.count("!")
    reticencias=texto.count("...")
    ponto=texto.count(".")
    reticencias2=(reticencias*3)
    if "..." in frase:
    return (ponto+interrogacao+exclamacao+reticencias-reticencias2):
    else:
        return (ponto+interrogacao+exclamacao)