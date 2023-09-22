def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    reticencias = texto.replace('...','.')
    if (texto.count('.')) and (texto.count('!')) and (texto.count('...')) and (texto.count('?')) in texto == True:
        return (texto.count('.')) + (texto.count('!')) + (texto.count('...')) + (texto.count('?'))