def conta_frases(texto):
    """" Função que enumera o numero de frases presentes no parametro
    str -> int"""
    ponto=str.count(texto,'.')
    reticencias=str.count(texto,'...')
    interrogacao=str.count9texto,'?')
    exclamacao=str.count(texto,'!')
    return ponto -3*reticencias*reticencias*interrogacao*exclamacao