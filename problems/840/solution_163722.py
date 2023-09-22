from math import min

def bolos (A, B, C):
    """calcula a quantidade máxima de bolos possíveis de serem feitos dados a quantidade de xícaras de farinha
       de trigo (A), ovos (B) e colheres de sopa de leite (C) dísponíveis, sabendo que para um bolo ser prepa-
       rado são necessários 2, 3 e 5 de cada ingrediente, respectivamente."""
    return min(A//2,B//3,C//5)