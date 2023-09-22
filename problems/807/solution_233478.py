def conta_frases(texto):
    final = texto.split(". ")
    exclamacao = texto.split("! ")
    interrogacao = texto.split("? ")
    reticencias = texto.split("... ")
    total = len(final) + len(exclamacao) + len(interrogacao) + len(reticencias)
    frases = (total + 1)/2
    return frases