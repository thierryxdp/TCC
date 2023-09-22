def bolos(A,B,C):
"""Determina a quantidade máxima de bolos que João pode fazer, dados os parâmetros
   a (xícaras de farinha de trigo) b (ovos) e c (colheres de sopa de leite);
   float,int,float->int"""
    return min(A//2,B//3,C//5)