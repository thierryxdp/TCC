def colchao(medidas,portaH,portaL):
    """funcao calcula e retorna se um conchao com suas determinadas passa pelas medidas da porta.
    int,int-->string"""
    if medidas[0]>portaH[1]:
        entra=False
    else:
        entra=True