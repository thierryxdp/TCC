def conta_frases(texto):
    """dado um texto retorna o número de frases que contem neste
    str->int"""
    textoAlterado = texto
    '...'='#'
    numeroFrases = texto.count('!')
    numeroFrases += texto.count('?')
    numeroFrases += texto.count('#')
    numeroFrases += texto.count('.')
    return numeroFrases