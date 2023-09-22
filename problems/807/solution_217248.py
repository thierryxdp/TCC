def conta_frases(texto):
    """Funcao que calcula e retorna o numero de frases que aparece no texto
    lista->lista"""
    ponto=str.count(texto,'.')
    interrogacao=str.count(texto,'?')
    exclamacao=str.count(texto,'!')
    reticencias=str.count(texto,'...')
    return ponto+interrogacao+exclamacao-3*reticencias+reticencias