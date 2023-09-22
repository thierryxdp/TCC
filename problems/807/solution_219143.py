def conta_frases(texto):
    """Função que dado um texto retorna o número de
       frases contidos nele.
       str->int"""
    interrogacao = str.count(texto,'!')
    exclamacao = str.count(texto,'?')
    ponto = str.count(texto,'.')
    reticencias = str.count(texto,'.') * 3
    soma = interrogacao + exclamacao + ponto - reticencias
    return soma