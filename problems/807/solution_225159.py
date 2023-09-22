def conta_frases(frases):
    '''função que determina o número de frases em uma certa
    sequência, as frases são identificadas a cada pontuação
    (... , . , ? e !) '''
    frases = 0
    """reticências na frase """
    reticencias = frase.count ( "..." )
    frases += reticencias
    """ pontos finais na frase """
    pontos_finais = frase.count ( "." )
    pontos_finais -= reticencias * 3
    frases += pontos_finais
    """ interrogações na frase """
    interrogacoes = frase.count ( "?" )
    frases += interrogacoes
    """exclamações na frase """
    exclamacoes = frase.count ( "!" )
    frases += exclamacoes
    return frases