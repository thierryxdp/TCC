def conta_frases(texto):
    '''
    	Funcao que recebe um texto e conta o numero de frases
        que aparecem neste texto
        string -> int
    '''
    x = texto.partition('.')
    y = texto.partition('!')
    z = texto.partition('?')
    p = texto.partition('...')
    return len(x)