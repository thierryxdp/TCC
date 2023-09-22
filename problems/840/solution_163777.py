def bolos(A,B,C):
  """achar a quantidade minima de bolos que podem ser feitos"""
    return min(farinha(A),ovos(B),leite(C))
def farinha(A):
    """calcular a quantidade de bolos por farinha"""
    return A/2
def ovos(B):
    """calcular a quantidade de bolos por ovos"""
    return B/3
def leite(C):
    """calcular a quantidade de bolos por colher de leite"""
    return C/5