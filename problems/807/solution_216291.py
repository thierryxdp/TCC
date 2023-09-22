def conta_frases(frase):
    """..."""
    ponto = str.count(frase,'.')
    exclamacao = str.count(frase,'!')
    interrogacao = str.count(frase,'?')
    reticencias = str.count(frase,'...')
    
    return ponto + exclamacao + interrogacao + reticencias-3*reticencias