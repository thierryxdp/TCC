def concatennacao(a,b):
    """Função que concatena duas strings a e b"""
    #entrada ab
    #retorno abba
    y = a+b
    return y+y[::-1]