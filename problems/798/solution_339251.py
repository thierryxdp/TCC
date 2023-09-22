def freq_palavras(frases):
    """ Função que recebe uma mensagem e retorna o número de
    frequências de cada palavra dessa mensagem.
    Entrada: str
    Saída: dict
    """
    
    palavras = {}
    for ' ' in frases:
        particao = frases.partition(espaco)
        palavras[particao[0]] = frases.count(particao[0])
        frases = particao[2]
   	
    return palavras