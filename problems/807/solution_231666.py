def conta_frases(texto):
    """
    	Recebe um texto e retorna a quantidade de frases
        contidas no texto.
        str --> int
    """
    pontoFinal = len(str.split(texto, '.'))-1
    exclamacao = len(str.split(texto, '!'))-1
    interrogacao = len(str.split(texto, '?'))-1
    reticencias = len(str.split(texto, '...'))-1
    qtdFrases = pontoFinal + exclamacao + interrogacao + reticencias
    return qtdFrases