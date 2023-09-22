def conta_frases(frase):
    '''Essa funcao conta frases. Recebe como parametro uma stringque considera como separador
    de frase "ponto final", "exclamacao","interrogacao", e "reticencias"
    '''
    return (frase.count('. ') + frase.count('! ') + frase.count('? ') + frase.count('... '))