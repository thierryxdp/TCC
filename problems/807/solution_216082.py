def conta_frases(texto):
    """função que retorna o número de frases contidas em um 
       texto. 
       str -> int"""
    ponto_final = texto.count('.')
    ponto_exclamacao = texto.count('!')
    ponto_interrogacao = texto.count('?')
    reticencias = texto. count('...')
    
    return ponto_final + ponto_exclamacao + ponto_interrogacao + reticencias