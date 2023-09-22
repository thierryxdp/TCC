from math import min
def bolos(A, B, C):
	"""Calcula e retorna a quantidade de bolos capaz de serem feitos 
	com A, B e C, que representam respectivamente a quantiade de 
    xicaras de farinha de trigo, ovos, colheres de sopa de leite;
    int, int ,int --> int"""
    return min(A//2, B//3, C//5)