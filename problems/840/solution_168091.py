import math
def bolos(a, b, c)
	"""Função que calcula e retorna a quantidade máxima de bolos dados os ingredientes mínimos para cada bolo, sendo (a) 2 xícaras de farinha, (b) 3 ovos e (c) 5 colhers de sopa de leite"""
    return math.floor(min((a/2),(b/3),(c/5)))