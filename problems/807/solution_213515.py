def conta_frases(texto):
    """ 
    Função que dado um texto, retorna a quantidade de frases.
    Cada frase pode ser terminada em ponto final(.), ponto de exclamação(!), ponto de interrogação(?) ou reticências(...)
    str-> int
    
    Parameters:
    texto: Parâmetro do tipo str que representa o texto inserido
    """
    return str.count(texto, '. ') + str.count(texto,'! ') + str.count(texto, '? ') + 1