def conta_frases(texto):
    """
    	Recebe um texto e retorna a quantidade de frases
        contidas no texto.
        str --> int
    """
    pontoFinal = str.count(texto, '.')
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    reticencias = str.count(texto, '...')
    qtdFrases = pontoFinal + exclamacao + interrogacao + reticencias
    return qtdFrases