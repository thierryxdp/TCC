import math
def bolos (A,B,C):
    """A função calcula a quantidades de bolos que se pode fazer com
    certa quantidade de material usando as entradas:
    A=xícaras de farinha(qxf)
    B=ovos(qo)
    C=colheres de sopa de leite(qcsl)"""
    q_farinha = (A//2)
    q_ovos = (B//3)
    q_leite= (C//5)
    return min (q_farinha,q_ovos,q_leite)