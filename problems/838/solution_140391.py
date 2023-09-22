def num_bombons(d,p):
    """Número de bombons que pedrinho pode comprar com seu dinheiro.
    d(dinheiro), p(preço dos bombons)"""
    return min(round(d/p))