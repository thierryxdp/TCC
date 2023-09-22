def conta_frases(texto_armazenado):
    """Funcao que dado um texto armazenado em um string, retorna o numero total de frases. str=>int"""
    texto_armazenado = str.replace(texto_armazenado,'...', '#')
    return str.count(texto_armazenado,'?')+str.count(texto_armazenado,'!')+str.count(texto_armazenado,"...")+str.count(texto_armazenado,".")