def conta_frases(texto):
    """dado um texto retorna o número de frases que contem neste
    str->int"""
    textoAlterado = texto
    textoAlterado = textoAlterado.replace('...','#')
    numeroFrases = textoAlterado.count('!')
    numeroFrases += textoAlterado.count('?')
    numeroFrases += textoAlterado.count('#')
    numeroFrases += textoAlterado.count('.')
    return numeroFrases