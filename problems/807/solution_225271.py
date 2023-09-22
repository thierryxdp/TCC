def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    texto.replace('...','.')
    if (texto.count('...') and texto.count('?') and texto.count('!') and texto.count('.')) == True:
        return (texto.count('?') + texto.count('!')) +2
    elif texto.count('...') == True and (texto.count('?') and texto.count('!') and texto.count('.')) == False:
        return texto.count('...')