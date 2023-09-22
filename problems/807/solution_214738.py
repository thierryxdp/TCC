def conta_frases(frase):
    """ Função que conta a quantidade de frases em um texto """
    texto = frase.split(".", "!","...")
    nTexto = len(texto)
    return nTexto