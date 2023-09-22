def conta_frases(texto):
    """função que retorna o número de frases contidas em um 
       texto. 
       str -> int"""
    ponto_exclamacao = texto.count('!')
    ponto_interrogacao = texto.count('?')
    reticencias = texto. count('...')
    ponto_final = texto.count('.') 
    
    if ponto_final > 3 and reticencias != 0:
        return ponto_exclamacao + ponto_interrogacao + (ponto_final - reticencias)
    else:
        return ponto_exclamacao + ponto_interrogacao + reticencias + ponto_final