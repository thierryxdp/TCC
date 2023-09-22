def conta_frases(frase):
    """ Função que conta a quantidade de frases em um texto """
    texto = frase
    nTexto = len(str.partition(texto,".", "!","..."))
    return nTexto