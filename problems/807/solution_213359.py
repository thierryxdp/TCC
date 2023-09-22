def conta_frases(texto):
    """Função dado um texto armazenado em string retorna a quantidade de frases contidas nesse texto.
   """
    
    #texto  = str.strip(texto)
    texto  = str.split(texto)
    return len(texto)