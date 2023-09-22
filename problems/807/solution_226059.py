def conta_frases(texto:str)->int:
    """Conta o número de frases que aparecem em um texto."""
    texto1 = texto.replace('...','.')
    return texto1.count('.')+texto1.count('!')+texto1.count('?')