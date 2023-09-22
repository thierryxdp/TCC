def conta_frases(texto):
    interrogacao = str.count(texto, '?')
    exclamacao = str.count(texto, '!')
    ponto = str.count(texto, '.')
    reticencias = str.count(str.replace(texto, '...', '*'), '*')
    return interrogacao + exclamacao + ponto + reticencias