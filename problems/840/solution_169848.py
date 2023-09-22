import math
def bolos (A,B,C):
    """função que retorna a quantidade máxima de bolos que o João consegue fazer"""
	return math.lcm(A/2+B/3+C/5)