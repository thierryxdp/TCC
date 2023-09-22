def conta_frases(texto:str)->int:
    """Conta o número de frases que aparecem em um texto."""
    texto1 = texto.replace('...','.')
    texto2 = texto1.replace('?','.')
    texto3 = texto2.replace('!','.')
    return texto.count('.')