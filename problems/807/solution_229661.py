def conta_frases(texto):
    """
    Função que dado um texto, retorna o número de frases
    que tem o texto
    string ---> int
    """
    str.replace(texto,"?",".")
    str.replace(texto,"!",".")
    str.replace(texto,"...",".")
    return str.split(texto,".")