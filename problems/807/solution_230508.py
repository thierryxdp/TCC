def conta_frases(frase):
    ponto=frase.count(".")
    interrogacao=frase.count("?")
    exclamacao=frase.count("!")
    reticencias=frase.count("...")
    quant_pts = ponto + interrogacao + interrogacao + reticencias
    if reticencias >= 1:
        return quant_pts - reticencias*3
    else:
    return quant_pts