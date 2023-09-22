def conta_frases(texto):
    "Conta o número de frases que aparece no texto. str->int"
    ponto = str.split(texto, ".")
    exclamacao = str.split(texto, "!")
    interrogacao = str.split(texto, "?")
    reticencias = str.split(texto, "...")
    tot1 = len(ponto)
    tot2 = len(exclamacao)
    tot3 = len(interrogacao)
    tot4 = len(reticencias)
    return tot1+tot2+tot3+tot4