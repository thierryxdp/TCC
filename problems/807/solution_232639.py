def conta_frases(texto):
    """Função que faz alguma coisa. str->int"""
    interrogacao=str.count("?")
    exclamacao=str.count("!")
    reticencias=str.count("...")
    ponto=str.count(".")
    return (interrogacao, exclamacao, reticencias,ponto)