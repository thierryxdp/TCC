def colchao(medidas,portaH,portaL):
    """funcao calcula e retorna se um conchao com suas determinadas passa pelas medidas da porta.
    int,int-->string"""
    if medidas[1]>portaH and medidas[1]>portaL:
        entra=False
    else:
        entra=True
    return entra