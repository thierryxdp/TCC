def conta_frases(texto):
    """Retorna a quantidade de frases do texto
       Entrada: str
       Saída: int 
    """
    exclamação = str.count(texto, '!')
    ponto_final = str.count(texto, '.')
    interrogação = str.count(texto, '?')
    reticencias= str.count(texto, '...')
    return exclamação+ponto_final+interrogação-(2*reticencias)