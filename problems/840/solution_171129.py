def bolos (farinha, ovos, leite):
    """calcula o numero de bolos que João poderá fazer com os ingredientes
    informados; int,int,int->int"""
    nbolos = min((farinha//2),(ovos//3),(leite//5))
    return nbolos