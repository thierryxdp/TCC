def conta_frases(texto):
    """Função que faz alguma coisa. str->int"""
    interrogacao=texto.count("?")
    exclamacao=texto.count("!")
    reticencias=texto.count("...")
    ponto=texto.count(".")
    return (interrogacao, exclamacao, reticencias,ponto)