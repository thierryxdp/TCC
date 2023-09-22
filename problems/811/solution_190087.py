def colchao(medidas,H,L):
    """ 
    """
    medidas.sort(reverse=False)
    a = medidas[0:1]
    if a>H:
        return 'true'