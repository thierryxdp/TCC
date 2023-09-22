def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    if texto.count('?') and texto.count('.') == True and (texto.count('!') and texto.count('...')) == False:
        return texto.count('?')+texto.count('.')
    elif texto.count('.') and texto.count('!') and texto.count('?') == True and texto.count('...') == False:
        return texto.count('.')+texto.count('!')+texto.count('?')
    elif texto.count('?') == True and (texto.count('.') and texto.count('!') and texto.count('...')) == False:
        return texto.count('?')