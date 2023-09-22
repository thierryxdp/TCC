def conta_frases(texto):
    """Funcao que conte o número de frases que aparecem neste texto.
    string -> int"""
    ponto = str.count(texto, '.')
    reticencias = str.count(texto, '...')
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    
    return ponto -3*reticencias + reticencias + exclamacao + interrogacao