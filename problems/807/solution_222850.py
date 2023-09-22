conta_frases(texto):
    """
    	Retorna a quantidade de frases que existe no texto.
        str -> int
    """
    return texto.count('.') + texto.count('!') + texto.count('?') + texto.count('...') - 2*texto.count('...')