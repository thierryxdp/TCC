def conta_frases(texto):
    """Função que faz alguma coisa. str->int"""
    interrogacao=list.count("?")
    exclamacao=list.count("!")
    reticencias=list.count("...")
    ponto= list.count(".")
    return (interrogacao, exclamacao, reticencias,ponto)