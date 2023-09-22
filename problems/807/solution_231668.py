def conta_frases(texto):
    """
    	Recebe um texto e retorna a quantidade de frases
        contidas no texto.
        str --> int
    """
    pontoFinal = str.split(texto, '.')
    exclamacao = str.split(texto, '!')
    interrogacao = str.split(texto, '?')
    reticencias = str.split(texto, '...')
    qtdFrases = pontoFinal + exclamacao + interrogacao + reticencias
    return qtdFrases