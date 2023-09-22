def contafrases(texto):
    """funcao que conta quantas frases tem o texto;
    str->int"""
    interrogacao=str.count(texto,'?')
    exclamacao=str.count(texto,'!')
    ponto=str.count(texto,'.')
    reticen=str.count(texto, '...')
    return ponto - reticen*2 + interrogacao + exclamacao