def conta_frases(texto):
    """dado um texto a funcao retorna o numero de 
    frases contidas nele; str->int"""
    reticencias= str.join(".", str.split(texto, '...')
    interrogacao= str.join(".", str.split(texto, '?'))
    ponto_final= str.count(texto, '.')
    soma_de_frases=ponto_final
    return soma_de_frases