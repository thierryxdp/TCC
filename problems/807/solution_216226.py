def conta_frases(texto):
    '''função que retorna a quantidade defrases que aparecem em um texto: str->int'''
    ponto = str.count(texto,'.')
    reticencias = str.count(texto,'...')
    interrogacao = str.count(texto,'?')
    exclamacao = str.count(texto,'!')
    
    return ponto-3*reticencias+reticencias+interrocao+exclamacao