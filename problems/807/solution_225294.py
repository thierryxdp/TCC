def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    reticencias = texto.replace('...','.')
    if texto.count('...') and texto.count('?') and texto.count('!') and texto.count('.'):
        return (texto.count('?') + texto.count('!')) +2
    elif texto.count('...') == True and (texto.count('?') and texto.count('!') and texto.count('.')) == False:
        return texto.count('...')
    elif texto.count('.') == True and (texto.count('?') and texto.count('!') and texto.count('...')) == False:
        return texto.count('.')
    elif (texto.count('.') > 1) == True and (texto.count('?') and texto.count('!') and texto.count('...')) == False:
        return texto.count('.')
    elif (texto.count('.') > 1) and (texto.count('...') > 1) == True and (texto.count('?') and texto.count('!') and texto.count('...')) == False:
        return (texto.count('.') + texto.count(reticencias)