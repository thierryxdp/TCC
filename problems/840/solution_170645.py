def bolos(A,B,C):
    """ calcula e retorna o valor a maior quantidade que joão 
    pode fazer o bolo dados os parametros A,B,C
    A = xicaras de farinha de trigo
    B = ovos
    C = colheres de sopa"""
    return min(A//2,B//3,C//5)