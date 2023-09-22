def conta_frases(texto):
    pontoFinal = str.count(texto, '.')
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    reticencias = str.count(texto, '...')
    qtdFrases = pontoFinal + exclamacao + interrogacao + reticencias
    return qtdFrases