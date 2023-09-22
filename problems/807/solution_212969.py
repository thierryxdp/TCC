def conta_frases(texto):
    """Função que retorna o numero de frases que aparecem em um texto
    entrada: str
    retorno: int"""
    pontos = texto.count('.')
    interroga = texto.count('?')
    exclama = texto.count('!')
    reticencia = texto.count('...')
    return pontos+ interroga+ exclama- 2*reticencia