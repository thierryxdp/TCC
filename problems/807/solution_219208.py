def conta_frases(texto):
    """Função que dado um texto retorna o número de
       frases contidos nele.
       str->int"""
    exclamacao=str.count(texto,'!')
    interrogacao=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    ponto=str.count(texto,'.') - 3*str.count(texto,'...')
    
    return exclamacao + interrogacao + reticencias + ponto