def conta_frases(texto):
    """Função que dado um texto, conta o número de frasesno mesmo. str->int"""
    interrogacao=texto.count("?")
    exclamacao=texto.count("!")
    reticencias=texto.count("...")
    ponto=texto.count(".")
    reticencias2=(reticencias*3)
    if "..." in texto:
        return (ponto+interrogacao+exclamacao+reticencias-reticencias2)
    else:
        return (ponto+interrogacao+exclamacao)