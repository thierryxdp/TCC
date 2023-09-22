def conta_frases(texto):
    """
    	Recebe um texto e retorna a quantidade de frases
        contidas no texto.
        str --> int
    """
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    reticencias = str.count(texto, 3*'.')
    pontoFinal = str.count(texto, '.') - 3*reticencias
    qtdFrases = pontoFinal + exclamacao + interrogacao + reticencias
    return qtdFrases