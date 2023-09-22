def conta_frases(texto):
    interrogacao = str.count(texto, '?')
    exclamacao = str.count(texto, '!')
    reticencias = str.replace(texto, '...', '*')
    reticencias2 = str.count(reticencias, '*')
    ponto = str.count(reticencias, '. ')
    return interrogacao + exclamacao + ponto + reticencias