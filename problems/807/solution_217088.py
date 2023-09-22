def conta_frases(texto):
    """Função que dado um 'texto', retorna o número de frases que aparecem nesse texto; str -> int"""

    ponto= str.count(texto,".")
    reticencias= str.count(texto,"...")
    interrogacao= str.count(texto,"?")
    exclamacao= str.count(texto,"!")

    return ponto -3*reticencias+reticencias+interrogacao+exclamacao