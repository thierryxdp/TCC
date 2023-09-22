def conta_frases(texto):
    """Retorna a quantidade de frases do texto
       Entrada: str
       Saída: int 
    """
    exclamacao = str.count(texto, '!')
    ponto_final = str.count(texto, '.')
    interrogacao = str.count(texto, '?')
    reticencias= str.count(texto, '...')
    return exclamacao+ponto_final+interrogacao-(2*reticencias)