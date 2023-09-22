import print 
def bolos(A,B,C):
    """Calcula a quantidade máxima de bolos que Joâo é capaz de fazer com os ingredientes disponíveis.
    Sendo A= quantidade de farinha de trigo,
          B= quantidade de ovos,
          C= quantidade de leite.
    int, int -> int"""
    return print (min(A//2,B//3,C//5)